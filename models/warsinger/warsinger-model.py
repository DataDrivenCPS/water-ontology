# %%
from rdflib import Namespace, Graph, Literal, URIRef
import re
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library, Model
from buildingmotif.namespaces import bind_prefixes

# %%
# setup our buildingmotif instance
bm = BuildingMOTIF("sqlite://")

# create the model w/ a namespace
WBS = Namespace("urn:ex/")
S223 = Namespace("http://data.ashrae.org/standard223#")
wbs = Model.create(WBS)
bind_prefixes(wbs.graph)
wbs.graph.bind("wbs", WBS)
wbs.graph.bind("s223", S223)
wbs.graph.bind("nawi", Namespace("urn:nawi-water-ontology#"))
things = []

# %%
templates = Library.load(directory='../warsinger/templates')
s223 = Library.load(ontology_graph="../../s223/collections/MODEL_SP223_all-v1.0.ttl")

# %%
templates.get_templates()

# %%
tank_temp = templates.get_template_by_name('tank')
filter_temp = templates.get_template_by_name('filter')
pipe_temp = templates.get_template_by_name('pipe')
bladder_temp = templates.get_template_by_name('bladder')
membrane_module_temp = templates.get_template_by_name('membrane-module')
pump_temp = templates.get_template_by_name('pump')
valve_temp = templates.get_template_by_name('valve')
check_valve_temp = templates.get_template_by_name('check-valve')

# %%
membrane_module_temp = templates.get_template_by_name('membrane-module')

# %%
a = membrane_module_temp.get_dependencies()[2]

# %%
dependencies = membrane_module_temp.get_dependencies()
for dep in dependencies:
    # TODO: Shouldn't do this, only works for the simplest contained equipment e.g. membraine module
    if dep.args['name'] not in (['in', 'out', 'role']):
        print("WARNING: Automatically filling dependency for: ", dep.args['name'])
    

# %%
DEFAULT_MEDIUM = S223['Medium-Water']
# this needs correcting
CONTROL_MEDIUM = S223['Medium-Electricity']
ADD_ALL_CNX_RELATIONS = True
def remove_optional(graph):
    # TODO: Probably not supposed to do this, how should I actually use templates and optional params?
    # Probably a better way to compose templates - definitely for hasRole, not sure for mapsTo
    # Works for this case, not where there are more things stemming from optional params, maybe should instead be done with template builder or removing dependencies? 
    graph.update('DELETE {wbs:delete ?p ?o} WHERE { wbs:delete ?p ?o . }')
    graph.update('DELETE {?s ?p wbs:delete} WHERE { ?s ?p wbs:delete . }')

def create_equipment(equip_name, equip_temp, optional_dict = {}, in_medium = DEFAULT_MEDIUM, out_medium = DEFAULT_MEDIUM, role = None):
    equip_dict = {'in': WBS[f'{equip_name}-in'],
    'in-medium': in_medium,
    'name': WBS[f'{equip_name}'],
    'out': WBS[f'{equip_name}-out'],
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
        equip_graph = equip.evaluate({param: WBS['delete'] for param in equip.parameters})
        remove_optional(equip_graph)
    wbs.add_graph(equip_graph)
    return equip_dict

def connect_equipment(source_dict, target_dict, source_cp = 'out', target_cp = 'in', conn_temp = pipe_temp, all_relations = ADD_ALL_CNX_RELATIONS):
    # take dictionary of source_uri equipment and outlet equipment, and connect them
    # Having source_cp and target_cp as dictionary keys may be confusing
    source_uri = source_dict['name']
    target_uri = target_dict['name']
    source_cp_uri = source_dict[source_cp]
    target_cp_uri = target_dict[target_cp]
    connection_uri = WBS[f'conn-{get_uri_end(source_uri)}-to-{get_uri_end(target_uri)}']

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
        wbs.graph.add((source_uri, S223['connected'], target_uri))
        wbs.graph.add((source_uri, S223['connectedTo'], target_uri))

        # source_uri relationships
        wbs.graph.add((source_uri, S223['hasConnectionPoint'], source_cp_uri))
        wbs.graph.add((source_uri, S223['cnx'], source_cp_uri))
        # wbs.graph.add((source_cp_uri, S223['isConnectionPointOf'], source_uri))
        wbs.graph.add((source_uri, S223['connectedThrough'], connection_uri))

        # target_uri relationships
        wbs.graph.add((target_uri, S223['hasConnectionPoint'], target_cp_uri))
        wbs.graph.add((target_uri, S223['cnx'], target_cp_uri))
        # wbs.graph.add((target_cp_uri, S223['isConnectionPointOf'], target_uri))
        wbs.graph.add((target_uri, S223['connectedThrough'], connection_uri))

        # C relationships
        wbs.graph.add((connection_uri, S223['connectsTo'], target_uri))
        wbs.graph.add((connection_uri, S223['connectsFrom'], source_uri))
        wbs.graph.add((connection_uri, S223['cnx'], target_cp_uri))
        wbs.graph.add((connection_uri, S223['cnx'], source_cp_uri))

        # Connection point relationships
        wbs.graph.add((source_cp_uri, S223['connectsThrough'], connection_uri))
        wbs.graph.add((source_cp_uri, S223['connectsAt'], connection_uri))
        wbs.graph.add((target_cp_uri, S223['connectsThrough'], connection_uri))
        wbs.graph.add((target_cp_uri, S223['connectsAt'], connection_uri))
    wbs.add_graph(conn_graph)
    return conn_dict
def get_uri_end(uri_ref):
    uri_str = str(uri_ref)
    match = re.search(r'[^/#]+$', uri_str)
    if match:
        return match.group(0)
    else:
        print("No match found, providing empty string")
        return ""

def get_unique_uri(uri):
    base_uri = str(uri)
    # I guess start at 2 since first ones are not numbered
    count = 2
    new_uri = URIRef(base_uri)
    # Check if the URI already exists in the graph
    while (new_uri, None, None) in wbs.graph or (None, None, new_uri) in wbs.graph:
        # Append an incremented number if it already exists
        new_uri = URIRef(f"{base_uri}-{count}")
        count += 1
    return new_uri

def add_properties(target, property_names):
    prop_dict = {prop: WBS[f"{get_uri_end(target)}-{prop}"] for prop in property_names}
    for prop, prop_uri in prop_dict.items():
        property = templates.get_template_by_name(prop).evaluate({'name': prop_uri})
        wbs.add_graph(property)
        wbs.graph.add((target, S223['hasProperty'], prop_uri))
    return prop_dict

def make_brine(salt_percent):
    # Takes salt percent as percent value between 0-100
    brine_temp = templates.get_template_by_name('brine')
    brine_dict = {
        'name': WBS[f'brine-{salt_percent}'],
        'salt-value': Literal(salt_percent),
        'salt-name': WBS[f'salt-{salt_percent}'],
        'water-value': Literal(100 - salt_percent),
        'water-name': WBS[f'water-{100-salt_percent}']
    }
    brine = brine_temp.inline_dependencies().evaluate(brine_dict)
    wbs.add_graph(brine)
    return brine_dict

def add_connection_point(equip_dict, cp_type = 'inlet-cp', medium = DEFAULT_MEDIUM):
    # could provide option to name point as input 
    name = get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-{cp_type}'])

    cp_dict = {
        'name': name,
        'medium': medium
    }
    cp_graph = templates.get_template_by_name(cp_type).inline_dependencies().evaluate(cp_dict)
    if isinstance(cp_graph, Graph):
        print("CP HAS ALL NEEDED PROPERTIES: ", name)
        cp_graph = cp_graph
    else:
        print("DELETING TEMPLATE PARAMETERS: ", cp_graph.parameters)
        cp_graph = cp_graph.evaluate({param: WBS['delete'] for param in cp_graph.parameters})
        remove_optional(cp_graph)
    wbs.add_graph(cp_graph)
    wbs.graph.add((equip_dict['name'], S223['hasConnectionPoint'], cp_dict['name']))
    wbs.graph.add((equip_dict['name'], S223['cnx'], cp_dict['name']))
    
    count = 1
    equip_cp_key = cp_type
    while equip_cp_key in equip_dict.keys():
        equip_cp_key = f'{cp_type}-{count}'
        count += 1
    equip_dict[equip_cp_key] = name
    return equip_cp_key

def add_vfd_to_pump(equip_dict, control_medium = CONTROL_MEDIUM):
    # Should be a controls medium, will update
    # partly mapped arguments in template, should decide what to do about that
    equip_dict.update({'vfd-name': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-vfd']), 
                        'pump-name': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-pump']), 
                        'elec-in': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-elec-in']),
                        'elec-in-medium': control_medium,
                        'pump-name-out-medium': equip_dict['in-medium'],
                        'pump-elec-in': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-pump-elec-in']), 
                        'pump-out': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-pump-out']), 
                        'on-off-command': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-on-off-command']),
                        'speed-command': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-speed-command']), 
                        'elec-medium': control_medium,
                        'vfd-name-out-medium': control_medium,
                        'vfd-out': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-vfd-out']),
                        'vfd-in': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-vfd-in']),
                        'vfd-name-in-medium': control_medium,
                        'pump-name-in-medium': equip_dict['in-medium'],
                        'pump-in': get_unique_uri(WBS[f'{get_uri_end(equip_dict["name"])}-pump-in']),})
    vfd_pump_graph = templates.get_template_by_name('pump-with-vfd').inline_dependencies().evaluate(equip_dict)
    if isinstance(vfd_pump_graph, Graph):
        print("PUMP WITH VFD HAS ALL NEEDED PROPERTIES: ", equip_dict['name'])
    else:
        print("DELETING TEMPLATE PARAMETERS: ", vfd_pump_graph.parameters)
        vfd_pump_graph = vfd_pump_graph.evaluate({param: WBS['delete'] for param in vfd_pump_graph.parameters})
        remove_optional(vfd_pump_graph)
    wbs.add_graph(vfd_pump_graph)
    return equip_dict
def add_controller(name, equip_dict_list, control_medium = CONTROL_MEDIUM):
    controller_dict = {'name': name}
    controller_graph = templates.get_template_by_name('controller').inline_dependencies().evaluate(controller_dict)
    wbs.add_graph(controller_graph)
    for equip_dict in equip_dict_list:
        cp_name = add_connection_point(controller_dict, 'outlet-cp', control_medium)
        connect_equipment(controller_dict, equip_dict,
                        cp_name,
                        'elec-in')
    return controller_dict
    

# %%
brine_temp = templates.get_template_by_name('brine').inline_dependencies()

# %%
make_brine(3.5)

# %%
# need to re-examine brine percentages, kind of random, not sure how many different percentages there are
supply_water_dict = make_brine(3.5)
pre_membrane_brine_water_dict = make_brine(10)
brine_water_dict = make_brine(20)
permeate_water_dict = make_brine(0.05)
# makeup shoulld be same as pre-membrane brine, but not sure

DEFAULT_MEDIUM = supply_water_dict['name']

supply_dict = create_equipment("supply-tank", tank_temp, role = S223['Role-Supply'])
supply_prop_dict = add_properties(supply_dict['out'], ['ph','temperature','conductivity'])
supply_valve_dict = create_equipment("supply-valve", valve_temp)
supply_conn_dict = connect_equipment(supply_dict, supply_valve_dict)
supply_filter_dict = create_equipment("supply-filter", filter_temp)
supply_valve_conn_dict = connect_equipment(supply_valve_dict, supply_filter_dict)

three_way_valve_1_dict = create_equipment("three-way-valve-1", valve_temp, out_medium=pre_membrane_brine_water_dict['name'])
three_way_valve_1_inlet_cp = add_connection_point(three_way_valve_1_dict, 'inlet-cp')
supply_filter_conn_dict = connect_equipment(supply_filter_dict, three_way_valve_1_dict)

DEFAULT_MEDIUM = pre_membrane_brine_water_dict['name']

# Pump should have VFD - other properties associated with that
circulation_pump_dict = create_equipment("circulation-pump", pump_temp)
three_way_valve_1_conn_dict = connect_equipment(three_way_valve_1_dict, circulation_pump_dict)
# Didn't asign a unit to pressure yet, maybe also want to make it differential on inlet and outlet of pump
circulation_pump_prop_dict = add_properties(circulation_pump_dict['name'], ['pressure'])
check_valve_dict = create_equipment("check-valve", check_valve_temp)
check_valve_prop_dict = add_properties(check_valve_dict['in'], ['flow-rate'])
circulation_pump_conn_dict = connect_equipment(circulation_pump_dict, check_valve_dict)
bladder_dict = create_equipment("bladder", bladder_temp)
check_valve_conn_dict = connect_equipment(check_valve_dict, bladder_dict)
check_valve_2_dict = create_equipment("check-valve-2", check_valve_temp)
bladder_conn_dict = connect_equipment(bladder_dict, check_valve_2_dict)
# Membrane module probably has multiple modules, may need to build it differently, also needs multiple connection points
membrane_module_dict = create_equipment("membrane-module", membrane_module_temp, out_medium=brine_water_dict['name'])
connect_equipment(check_valve_2_dict, membrane_module_dict)

DEFAULT_MEDIUM = brine_water_dict['name']

membrane_module_prop_dict = add_properties(membrane_module_dict['name'], ['pressure'])
relief_valve_dict = create_equipment("relief-valve", valve_temp, role = S223['Role-Relief'])
connect_equipment(membrane_module_dict, relief_valve_dict)
relief_valve_prop = add_properties(relief_valve_dict['out'], ['temperature'])

three_way_valve_2_dict = create_equipment("three-way-valve-2", valve_temp)
three_way_valve_2_outlet_cp = add_connection_point(three_way_valve_2_dict, 'outlet-cp')
connect_equipment(relief_valve_dict, three_way_valve_2_dict)
# connecting three way valves 
connect_equipment(three_way_valve_2_dict, three_way_valve_1_dict, source_cp = three_way_valve_2_outlet_cp, target_cp= three_way_valve_1_inlet_cp)

brine_tank_dict = create_equipment("brine-tank", tank_temp, in_medium=brine_water_dict['name'], out_medium=brine_water_dict['name'])
brine_tank_prop_dict = add_properties(brine_tank_dict['in'], ['ph','conductivity'])
connect_equipment(three_way_valve_1_dict, brine_tank_dict)

DEFAULT_MEDIUM = permeate_water_dict['name']

membrane_module_outlet_cp = add_connection_point(membrane_module_dict, 'outlet-cp')
permeate_valve_dict = create_equipment("permeate-valve", valve_temp)
connect_equipment(membrane_module_dict, permeate_valve_dict, source_cp = membrane_module_outlet_cp)
permeate_tank_dict = create_equipment("permeate-tank", tank_temp)
add_properties(permeate_tank_dict['in'], ['ph','flow-rate','conductivity'])
connect_equipment(permeate_valve_dict, permeate_tank_dict)

#Maybe it's just water in the makeup tank
DEFAULT_MEDIUM = S223['Medium-Water']

bladder_bidirectional_cp = add_connection_point(bladder_dict, 'bidirectional-cp')
bladder_valve_dict = create_equipment("bladder-valve", valve_temp)
bladder_valve_bidirectional_cp = add_connection_point(bladder_valve_dict, 'bidirectional-cp')
# Check if some inferencing or adjustment to this function is needed for bidirectional equips
connect_equipment(bladder_dict, bladder_valve_dict, source_cp = bladder_bidirectional_cp, target_cp = bladder_valve_bidirectional_cp)
check_valve_bladder_makeup_dict = create_equipment("check-valve-bladder-to-makeup", check_valve_temp)
connect_equipment(bladder_valve_dict, check_valve_bladder_makeup_dict)
check_valve_makeup_bladder_dict = create_equipment("check-valve-makeup-to-bladder", check_valve_temp)
connect_equipment(check_valve_makeup_bladder_dict, bladder_valve_dict)
# Rather than adding connection points - would probably be useful to create accurate templates that map 223P to brick-like objects
makeup_tank_dict = create_equipment("makeup-tank", tank_temp, role = S223['Role-Makeup'])
makeup_tank_valve_dict = create_equipment("makeup-tank-valve", valve_temp)
connect_equipment(makeup_tank_dict, makeup_tank_valve_dict)
makeup_tank_filter_dict = create_equipment("makeup-tank-filter", filter_temp)
connect_equipment(makeup_tank_valve_dict, makeup_tank_filter_dict)
# Filter needs VFD
high_pressure_pump_dict = create_equipment("high-pressure-pump", pump_temp)
connect_equipment(makeup_tank_filter_dict, high_pressure_pump_dict)
high_pressure_pump_relief_valve_dict = create_equipment("high-pressure-pump-relief-valve", pump_temp, role=S223['Role-Relief'])
connect_equipment(high_pressure_pump_dict, high_pressure_pump_relief_valve_dict)
# Perhaps these properties should be on the connection 
# Need a convention - properties not essential to an equipment are on the connection rather than inlet/outlet? Properties usually on inlet/outlets?
makeup_line_prop_dict = add_properties(check_valve_makeup_bladder_dict['in'], ['pressure','flow-rate'])


# %%
# adding control network 
circulation_pump_dict = add_vfd_to_pump(circulation_pump_dict)
high_pressure_pump_dict = add_vfd_to_pump(high_pressure_pump_dict)
# adding controller 
add_controller(WBS["pump-controller"], [circulation_pump_dict, high_pressure_pump_dict])

# %%
wbs.graph.serialize("warsinger-bladder-model.ttl", format="turtle")

# %%
# Create property graph for pyvis based on templates or dictionaries?
# Probably better to do based on queries. 

# %%
wbs.graph.parse('../../s223/collections/MODEL_SP223_all-v1.0.ttl', format="turtle")
# wbs.graph.parse('../../water/', format="turtle")


