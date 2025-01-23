from rdflib import Namespace, Graph, Literal, URIRef
import re
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library, Model
from buildingmotif.namespaces import bind_prefixes

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
S223 = Namespace("http://data.ashrae.org/standard223#")
DEFAULT_MEDIUM = S223['Medium-Water']
# this needs correcting
CONTROL_MEDIUM = S223['Medium-Electricity']
ADD_ALL_CNX_RELATIONS = True

def remove_optional(graph, ns):
        # TODO: Probably not supposed to do this, how should I actually use templates and optional params?
        # Probably a better way to compose templates - definitely for hasRole, not sure for mapsTo
        # Works for this case, not where there are more things stemming from optional params, maybe should instead be done with template builder or removing dependencies? 
        graph.update(f'DELETE {{{ns}:delete ?p ?o}} WHERE {{ {ns}:delete ?p ?o . }}')
        graph.update(f'DELETE {{?s ?p {ns}:delete}} WHERE {{ ?s ?p {ns}:delete . }}')

def get_uri_end(uri_ref):
    # I think I can also do this with quads or something, may be better than regex
    uri_str = str(uri_ref)
    match = re.search(r'[^/#]+$', uri_str)
    if match:
        return match.group(0)
    else:
        print("No match found, providing empty string")
        return ""

class ModelBuilder:
    def __init__(self, ns, bm_instance, templates):
        self.ns = ns
        self.bm = bm_instance
        self.graph = self.bm.graph
        self.templates = templates

    def create_equipment(self, equip_name, equip_temp_name, optional_dict = {}, in_medium = DEFAULT_MEDIUM, out_medium = DEFAULT_MEDIUM, role = None):
        equip_temp = self.templates.get_template_by_name(equip_temp_name)
        equip_dict = {'in': self.ns[f'{equip_name}-in'],
        'in-medium': in_medium,
        'name': self.ns[f'{equip_name}'],
        'out': self.ns[f'{equip_name}-out'],
        'out-medium': out_medium,
        }
        if role:
            equip_dict['role'] = role

        equip = equip_temp.inline_dependencies().evaluate(equip_dict)
        if isinstance(equip, Graph):
            print("EQUIP HAS ALL NEEDED PROPERTIES: ", equip_name)
            equip_graph = equip
        else:
            print("DELETING TEMPLATE PARAMETERS: ", equip.parameters)
            equip_graph = equip.evaluate({param: self.ns['delete'] for param in equip.parameters})
            remove_optional(equip_graph)
        self.bm.add_graph(equip_graph)
        return equip_dict

    def connect_equipment(self, source_dict, target_dict, source_cp = 'out', target_cp = 'in', conn_temp_name = 'pipe', all_relations = ADD_ALL_CNX_RELATIONS):
        # take dictionary of source_uri equipment and outlet equipment, and connect them
        # Having source_cp and target_cp as dictionary keys may be confusing
        # pipe is the default connection 
        conn_temp = self.templates.get_template_by_name(conn_temp_name)
        source_uri = source_dict['name']
        target_uri = target_dict['name']
        source_cp_uri = source_dict[source_cp]
        target_cp_uri = target_dict[target_cp]
        connection_uri = self.ns[f'conn-{get_uri_end(source_uri)}-to-{get_uri_end(target_uri)}']

        conn_dict = {
                'in': source_cp_uri,
                'out': target_cp_uri,
                'name': connection_uri
            }
        # Template doesn't actually rely on in and out, just keeping these names for consistency
        conn_graph = conn_temp.inline_dependencies().evaluate(conn_dict)
        # Just adding these so we can skip inference, all below programmatically added by inference rules

        if all_relations:
            # Top level connections
            self.bm.graph.add((source_uri, S223['connected'], target_uri))
            self.bm.graph.add((source_uri, S223['connectedTo'], target_uri))

            # source_uri relationships
            self.bm.graph.add((source_uri, S223['hasConnectionPoint'], source_cp_uri))
            self.bm.graph.add((source_uri, S223['cnx'], source_cp_uri))
            # self.bm.graph.add((source_cp_uri, S223['isConnectionPointOf'], source_uri))
            self.bm.graph.add((source_uri, S223['connectedThrough'], connection_uri))

            # target_uri relationships
            self.bm.graph.add((target_uri, S223['hasConnectionPoint'], target_cp_uri))
            self.bm.graph.add((target_uri, S223['cnx'], target_cp_uri))
            # self.bm.graph.add((target_cp_uri, S223['isConnectionPointOf'], target_uri))
            self.bm.graph.add((target_uri, S223['connectedThrough'], connection_uri))

            # C relationships
            self.bm.graph.add((connection_uri, S223['connectsTo'], target_uri))
            self.bm.graph.add((connection_uri, S223['connectsFrom'], source_uri))
            self.bm.graph.add((connection_uri, S223['cnx'], target_cp_uri))
            self.bm.graph.add((connection_uri, S223['cnx'], source_cp_uri))

            # Connection point relationships
            self.bm.graph.add((source_cp_uri, S223['connectsThrough'], connection_uri))
            self.bm.graph.add((source_cp_uri, S223['connectsAt'], connection_uri))
            self.bm.graph.add((target_cp_uri, S223['connectsThrough'], connection_uri))
            self.bm.graph.add((target_cp_uri, S223['connectsAt'], connection_uri))
        self.bm.add_graph(conn_graph)
        return conn_dict

    def add_to_connection(self, source_dict, target_dict, source_cp = 'out', target_cp = 'in', source_is_conn = True, all_relations = ADD_ALL_CNX_RELATIONS):
        # Either source or target can be a connection, is source_is_conn is true, source is connection, if false, target is connection

        if source_is_conn:
            connection_uri = source_dict['name']
            target_cp_uri = target_dict[target_cp]
            target_uri = target_dict['name']
            self.bm.graph.add((connection_uri, S223['cnx'], target_cp_uri))
            
            if all_relations:

                # target_uri relationships
                self.bm.graph.add((target_uri, S223['hasConnectionPoint'], target_cp_uri))
                self.bm.graph.add((target_uri, S223['cnx'], target_cp_uri))
                # self.bm.graph.add((target_cp_uri, S223['isConnectionPointOf'], target_uri))
                self.bm.graph.add((target_uri, S223['connectedThrough'], connection_uri))

                # C relationships
                self.bm.graph.add((connection_uri, S223['connectsTo'], target_uri))
                self.bm.graph.add((connection_uri, S223['cnx'], target_cp_uri))

                # Connection point relationships
                self.bm.graph.add((target_cp_uri, S223['connectsThrough'], connection_uri))
                self.bm.graph.add((target_cp_uri, S223['connectsAt'], connection_uri))
                
        else:
            connection_uri = target_dict['name']
            source_cp_uri = source_dict[source_cp]
            source_uri = source_dict['name']
            self.bm.graph.add((source_cp_uri, S223['cnx'], connection_uri))

            if all_relations:

                # source_uri relationships
                self.bm.graph.add((source_uri, S223['hasConnectionPoint'], source_cp_uri))
                self.bm.graph.add((source_uri, S223['cnx'], source_cp_uri))
                self.bm.graph.add((source_uri, S223['connectedThrough'], connection_uri))

                self.bm.graph.add((connection_uri, S223['connectsFrom'], source_uri))
                self.bm.graph.add((connection_uri, S223['cnx'], source_cp_uri))

                # Connection point relationships
                self.bm.graph.add((source_cp_uri, S223['connectsThrough'], connection_uri))
                self.bm.graph.add((source_cp_uri, S223['connectsAt'], connection_uri))

    def get_unique_uri(self, uri):
        base_uri = str(uri)
        # I guess start at 2 since first ones are not numbered
        count = 2
        new_uri = URIRef(base_uri)
        # Check if the URI already exists in the graph
        while (new_uri, None, None) in self.graph or (None, None, new_uri) in self.graph:
            # Append an incremented number if it already exists
            new_uri = URIRef(f"{base_uri}-{count}")
            count += 1
        return new_uri

    def add_properties(self,target, property_names, comments = None):
        prop_dict = {prop: self.get_unique_uri(self.ns[f"{get_uri_end(target)}-{prop}"]) for prop in property_names}
        # messy way to add coments and unique uri, but ok
        for i, (prop, prop_uri) in enumerate(prop_dict.items()):
            property = self.templates.get_template_by_name(prop).evaluate({'name': prop_uri})
            self.bm.add_graph(property)
            self.bm.graph.add((target, S223['hasProperty'], prop_uri))
            if comments:
                if comments[i]:
                    self.bm.graph.add((prop_uri, RDFS['comment'], Literal(str(comments[i]))))
        return prop_dict

    def make_brine(self, salt_percent):
        # Takes salt percent as percent value between 0-100
        brine_temp = self.templates.get_template_by_name('brine')
        brine_dict = {
            'name': self.ns[f'brine-{salt_percent}'],
            'salt-value': Literal(salt_percent),
            'salt-name': self.ns[f'salt-{salt_percent}'],
            'water-value': Literal(100 - salt_percent),
            'water-name': self.ns[f'water-{100-salt_percent}']
        }
        brine = brine_temp.inline_dependencies().evaluate(brine_dict)
        self.bm.add_graph(brine)
        return brine_dict

    def add_connection_point(self, equip_dict, cp_type = 'inlet-cp', medium = DEFAULT_MEDIUM):
        # could provide option to name point as input 
        name = self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-{cp_type}'])

        cp_dict = {
            'name': name,
            'medium': medium
        }
        cp_graph = self.templates.get_template_by_name(cp_type).inline_dependencies().evaluate(cp_dict)
        if isinstance(cp_graph, Graph):
            print("CP HAS ALL NEEDED PROPERTIES: ", name)
            cp_graph = cp_graph
        else:
            print("DELETING TEMPLATE PARAMETERS: ", cp_graph.parameters)
            cp_graph = cp_graph.evaluate({param: self.ns['delete'] for param in cp_graph.parameters})
            remove_optional(cp_graph)
        self.bm.add_graph(cp_graph)
        self.bm.graph.add((equip_dict['name'], S223['hasConnectionPoint'], cp_dict['name']))
        self.bm.graph.add((equip_dict['name'], S223['cnx'], cp_dict['name']))
        
        count = 1
        equip_cp_key = cp_type
        while equip_cp_key in equip_dict.keys():
            equip_cp_key = f'{cp_type}-{count}'
            count += 1
        equip_dict[equip_cp_key] = name
        return equip_cp_key

    def add_vfd_to_pump(self, equip_dict, control_medium = CONTROL_MEDIUM):
        # Should be a controls medium, will update
        # partly mapped arguments in template, should decide what to do about that
        equip_dict.update({'vfd-name': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-vfd']), 
                            'pump-name': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-pump']), 
                            'elec-in': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-elec-in']),
                            'elec-in-medium': control_medium,
                            'pump-name-out-medium': equip_dict['in-medium'],
                            'pump-elec-in': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-pump-elec-in']), 
                            'pump-out': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-pump-out']), 
                            'on-off-command': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-on-off-command']),
                            'speed-command': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-speed-command']), 
                            'elec-medium': control_medium,
                            'vfd-name-out-medium': control_medium,
                            'vfd-out': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-vfd-out']),
                            'vfd-in': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-vfd-in']),
                            'vfd-name-in-medium': control_medium,
                            'pump-name-in-medium': equip_dict['in-medium'],
                            'pump-in': self.get_unique_uri(self.ns[f'{get_uri_end(equip_dict["name"])}-pump-in']),})
        vfd_pump_graph = self.templates.get_template_by_name('pump-with-vfd').inline_dependencies().evaluate(equip_dict)
        if isinstance(vfd_pump_graph, Graph):
            print("PUMP WITH VFD HAS ALL NEEDED PROPERTIES: ", equip_dict['name'])
        else:
            print("DELETING TEMPLATE PARAMETERS: ", vfd_pump_graph.parameters)
            vfd_pump_graph = vfd_pump_graph.evaluate({param: self.ns['delete'] for param in vfd_pump_graph.parameters})
            remove_optional(vfd_pump_graph)
        self.bm.add_graph(vfd_pump_graph)
        return equip_dict
    def add_controller(self, name, equip_dict_list, control_medium = CONTROL_MEDIUM):
        controller_dict = {'name': name}
        controller_graph = self.templates.get_template_by_name('controller').inline_dependencies().evaluate(controller_dict)
        self.bm.add_graph(controller_graph)
        for equip_dict in equip_dict_list:
            cp_name = self.add_connection_point(controller_dict, 'outlet-cp', control_medium)
            self.connect_equipment(controller_dict, equip_dict,
                            cp_name,
                            'elec-in')
        return controller_dict
    