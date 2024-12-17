import os
import re
import subprocess

import click
import pyvis
from rdflib import Graph, Literal, Namespace

from rdf2html_classification import (
    EdgesConfig,
    bacnet_labels,
    is_wanted_node,
    propgraph_labels,
    s223_types,
    skip_edges,
)

g = Graph()
nodes = {}


def parse_rdf(ttl_file):
    global g
    assert os.path.exists(ttl_file)
    # with open(os.path.abspath(ttl_file), "r") as ttl:
    #     lines = ttl.read()
    graph = Graph()
    graph.parse(ttl_file, format = 'ttl')
    # graph = g.parse(data=lines, format="turtle")
    # graph = constraint_label(graph)
    # graph = return_in_distance(graph)
    # updates(graph)
    return graph

class Node:
    groups = {
        "Equipment": {
            "size": 20,
            "color": "green",
            "shape": "square",
            "group_int": 1,
            "borderWidth": None,
            "uri": "vis:legend/Equipment",
            "label": "Legend / Equipment",
        },
        "Contained-Equipment": {
            "size": 10,
            "color": "yellow",
            "shape": "square",
            "group_int": 1,
            "borderWidth": None,
            "uri": "vis:legend/Contained-Equipment",
            "label": "Legend / Contained-Equipment",
        },
        "Default": {
            "size": 15,
            "color": None,
            "shape": "dot",
            "group_int": 0,
            "borderWidth": None,
            "uri": "vis:legend/Default",
            "label": "Legend / Default",
        },
    }

    def __init__(self, s, p=None, o=None):
        self.ns = set()
        self.types = set()
        self.label = None
        self.comment = None
        self.value = None
        self.level = None
        self.uri = str(s)

        self.properties = {}
        for k, v in propgraph_labels.items():
            self.properties[k] = set()

        self.properties["bacnet"] = {}

        if p and o:
            if "http://www.w3.org/1999/02/22-rdf-syntax-ns#type" in p:
                self.ns.add(str(o))
            self.add_info(s, p, o)
            if "label" not in p and "comment" not in p:
                self.namespace_and_type(o)
        else:
            self.namespace_and_type(s)

    def namespace_and_type(self, info):
        if "urn" in info:
            return
        try:
            ns, _type = prefix(info)
            self.ns.add(ns)
            self.types.add(_type)
        except TypeError:
            pass

    # @property
    # def group_name(self):
    #     for k, v in s223_types.items():
    #         for each in v:
    #             if each in self.types:
    #                 return k
    #     return "Default"
    @property
    def group_name(self):
        g.query("""ASK {?s a/s223:subClassOf* s223:Equipment .}""")
        for contained_equipment in g.objects(None, "s223:contains"):
            if contained_equipment in nodes:
                nodes[contained_equipment].group_name = "Contained-Equipment"
        return "Default"
    @property
    def group(self):
        return self.groups[self.group_name]["group_int"]

    @property
    def size(self):
        return self.groups[self.group_name]["size"]

    @property
    def color(self):
        return self.groups[self.group_name]["color"]

    @property
    def shape(self):
        return self.groups[self.group_name]["shape"]

    @property
    def borderWidth(self):
        return self.groups[self.group_name]["borderWidth"]

    @property
    def title(self):
        _bubble = ""
        _n = ", ".join(self.ns)
        _t = ", ".join(self.types)
        _bubble += f"Label : {self.label}"
        _bubble += f"\n======="
        if self.uri:
            _bubble += f"\nURI : {self.uri}"
        _bubble += f"\nNamespaces : {_n}\nTypes: {_t}"
        if self.comment:
            _bubble += f"\n=======\n"
            _bubble += f"\nComment : {self.comment}"
            _bubble += f"\n======="
        if self.value:
            _bubble += f"\nValue : {self.value}"
        if self.properties.values():
            _bubble += f"\n======="
        for k, v in self.properties.items():
            try:
                if v:
                    _v = ", ".join(v)
                    _bubble += f"\n  - {k} : {_v}"
            except TypeError as error:
                print(f"Error processing {k,v}")

        if self.properties["bacnet"]:
            for k, v in self.properties["bacnet"].items():
                _bubble += f"\n{k} : {v}"

        return _bubble

    def add_info(self, s, p, o):
        def format_value(_o):
            if isinstance(_o, Literal):
                _v = str(_o)
            else:
                _v = prefix(str(_o))[1]
            # print(_o, _v)
            return _v

        if "label" in p:
            self.label = str(o)
        elif "comment" in p:
            self.comment = str(o)
        elif "ns#type" in p:
            self.namespace_and_type(o)
        elif "level" in p:
            self.level = str(o)

        for k, v in propgraph_labels.items():
            for each in v:
                if each in p:
                    if k in self.properties.keys():
                        self.properties[k].add(format_value(o))
                    else:
                        # print(f"adding direct node prop : {k} | {v} | {each}")
                        setattr(self, k, format_value(o))
        for k, v in bacnet_labels.items():
            if v in p:
                self.properties["bacnet"][k] = format_value(o)


def prepare_nodes(g):
    global nodes
    for s, p, o in g:
        if s not in nodes.keys():
            # print(f"Adding {s}")
            nodes[s] = Node(s, p, o)
        else:
            # print(f"Modifying {s} -> {nodes[s].uri}")
            nodes[s].add_info(s, p, o)
        if o not in nodes.keys() and is_wanted_node(prefix(p)[1]):
            nodes[o] = Node(o)


def make_legend(g):
    # Add Legend Nodes
    step = 100
    x = 2000
    y = -1000
    for k, v in Node.groups.items():
        g.add_node(
            v["uri"],
            group=v["group_int"],
            label=v["label"],
            size=v["size"],
            borderWidth=v["borderWidth"],
            # 'fixed': True, # So that we can move the legend nodes around to arrange them better
            physics=False,
            x=x,
            y=f"{y + v['group_int']*step}px",
            shape=v["shape"],
            widthConstraint=500,
            font={"size": 20},
        )


def prefix(full):
    _prefixes = [
        ("owl", "http://www.w3.org/2002/07/owl#"),
        ("quantitykind", "http://qudt.org/vocab/quantitykind/"),
        ("qudt", "http://qudt.org/schema/qudt/"),
        ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
        ("s223", "http://data.ashrae.org/standard223#"),
        ("unit", "http://qudt.org/vocab/unit/"),
        ("xsd", "http://www.w3.org/2001/XMLSchema#"),
        ("rec", "https://w3id.org/rec/core/"),
        ("sh", "http://www.w3.org/ns/shacl#"),
        ("equip", "urn:nawi-water-ontology/equip#")
    ]
    for each in _prefixes:
        _p, _f = each
        if _f in full:
            return (_p, full.replace(_f, f"{_p}:"))
    return (full, full)


def to_html(ttl_file, filter_urn=False, remove_basic_classes=False, show=False):
    global g, nodes
    g = parse_rdf(ttl_file)
    prepare_nodes(g)

    visual_graph = pyvis.network.Network(
        select_menu=True, filter_menu=True, cdn_resources="remote", directed=True
    )

    for k, v in nodes.items():
        # print(f"Adding to viz : {v.uri}")
        if set(['s223:InletConnectionPoint', 's223:OutletConnectionPoint', 's223:Connection','s223:BidirectionalConnectionPoint']) & v.types:
            continue
        if v.group == 2:
            v.label = "Connection" if not v.label else v.label

        visual_graph.add_node(
            v.uri,
            v.label,
            level = v.level,
            title=v.title,
            size=v.size,
            color=v.color,
            shape=v.shape,
            group=v.group,
            borderWidth=v.borderWidth,
        )

    for s, p, o in g:
        # TODO : if not s223 namespace : dashes
        try:
            _prefix, title = prefix(str(p))
            if title in skip_edges:
                continue
            _config = EdgesConfig(_prefix, title)
            _dashes = False if _prefix == "s223" else True
            visual_graph.add_edge(str(s), str(o), **_config.args)
        except AssertionError as error:
            # print(f"Problem adding edge to {s} | {p} | {o} : {error}")
            continue  # we don't want thoses nodes (aspects, medium, label, etc.)

    make_legend(visual_graph)

    visual_graph.toggle_physics(True)
    visual_graph.show_buttons(True)
    # usually false
    visual_graph.set_edge_smooth("dynamic")
    html_filename = f"{ttl_file.split('.ttl')[0]}.html"
    if show:
        visual_graph.show(html_filename, notebook=False)
    else:
        visual_graph.write_html(html_filename, notebook=False)
    visual_graph = None
    del visual_graph


def find_ttl_files(folder, found=[]):
    ttl_name_std = re.compile(r".ttl$")
    files_found = found
    for each in list(os.scandir(folder)):
        # print(each)
        if each.is_file():
            file = each.name
            # print('Name : ', file)
            if ttl_name_std.search(file):
                # print('Found : ', file)
                files_found.append(os.path.join(folder, file))
        elif each.is_dir() and each.name not in (".", ".git"):
            find_ttl_files(each, found=files_found)
    return files_found


def clear() -> None:
    """Remove all the triples from the graph, reset the blank node counter."""
    global g
    # remove all the triples
    g.remove((None, None, None))
    del g
    g = Graph()


def convert_all(folder):
    files = find_ttl_files(folder)
    for each in files:
        p = os.path.normpath(each)
        print(f"Processing {p}")
        subprocess.run(
            ["rdf2html", p]
        )  # using run assure nothing is kept in memory so new graphs are created for each file
        clear()

# adding the label for constraints
def constraint_label(graph):
    construct = """ 
        prefix ex: <http://example.org#> 
        PREFIX s223: <http://data.ashrae.org/standard223#>
        PREFIX sh: <http://www.w3.org/ns/shacl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>


        CONSTRUCT {
        ?s rdfs:label ?newString .
        }
        # SELECT ?newString ?o
        WHERE {
        ?s sh:path ?o .
        BIND(replace(concat(str(?o), " Constraint"), "http://data.ashrae.org/standard223#", "") AS ?newString).
        }

        """
    return graph.query(construct).graph + graph

def return_in_distance(graph):
    return_in_distance= """ 
        prefix ex: <http://example.org#> 
        PREFIX s223: <http://data.ashrae.org/standard223#>
        PREFIX sh: <http://www.w3.org/ns/shacl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>


        CONSTRUCT {
        ?s a s223:Equipment .
        ?s ?p ?o .
        ?o rdfs:label ?o2 .
        ?o rdfs:comment ?c .
        }
        # SELECT * 
        WHERE {
        ?s rdf:type/rdfs:subClassOf* s223:Class .
        ?s ?p ?o .
        OPTIONAL {?o rdfs:label ?o2 .}
        OPTIONAL {?o rdfs:comment ?c .}
        # FILTER(?o2 != ?s)
        }

        """ 
    return_list=  """ 
        prefix ex: <http://example.org#> 
        PREFIX s223: <http://data.ashrae.org/standard223#>
        PREFIX sh: <http://www.w3.org/ns/shacl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>


        CONSTRUCT {
                ?s a s223:Equipment .
                ?s sh:property ?op3 .
                ?op3 rdfs:label ?o2 .
                ?op3 rdfs:comment ?c .
                }
        # SELECT * 
        WHERE {
        ?s rdf:type/rdfs:subClassOf* s223:Class .
        ?s sh:or|sh:and|sh:xone ?o .
        ?o rdf:rest*/rdf:first ?op2 .
        ?op2 sh:property ?op3 .
        ?op3 ?p4 ?op4.
        OPTIONAL {?op3 rdfs:label ?o2 .}
        ?op3 rdfs:comment ?c .
        }

        """
    # graph.serialize('temp.ttl', format = 'ttl')
    g2 = Graph()
    g2 = g2 + graph.query(return_list).graph
    g2.serialize('temp.ttl', format = 'ttl')
    g2 = g2 + graph.query(return_in_distance).graph 
    g2.bind("s223", Namespace("http://data.ashrae.org/standard223#"))
    g2.bind("sh", Namespace("http://www.w3.org/ns/shacl#"))
    g2.serialize('temp2.ttl', format = 'ttl')
    g = Graph()
    return g.parse('temp2.ttl', format = 'ttl')



@click.command()
@click.argument("source", type=click.Path())
@click.option("-v", "--view", default=False)
def process(source=None, view=False):
    if os.path.isfile(source):
        to_html(source, show=view)
    else:
        convert_all(source)


if __name__ == "__main__":
    process()
    