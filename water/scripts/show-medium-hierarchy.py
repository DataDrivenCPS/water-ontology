#%%
from rdflib import Graph,RDF, RDFS, Namespace
import rdflib
from rich.tree import Tree
from rich import print
import sys
from utils import parse_ttl_files_in_directory, get_prefixes, query_to_df

def get_subclass_hierarchy(g, class_uri):
    query = f"""
    {get_prefixes(g)}
    SELECT ?subclass ?parent
    WHERE {{
        ?subclass rdfs:subClassOf+ {class_uri} .
        ?subclass rdfs:subClassOf ?parent .
        FILTER (?parent != ?subclass)
    }}
    """
    results = g.query(query)
    return results

def build_tree(g, class_uri, subclass_data):
    # Extract the local name of the class URI
    local_name = class_uri.split(':')[-1]
    tree = Tree(f"[bold]{local_name}[/bold]")
    children = {}
    
    for row in subclass_data:
        subclass = g.namespace_manager.compute_qname(row.subclass)[2]
        parent = g.namespace_manager.compute_qname(row.parent)[2]
        if parent not in children:
            children[parent] = []
        children[parent].append(subclass)
    
    def add_children(node, parent):
        if parent in children:
            for child in sorted(children[parent]):
                child_node = node.add(f"[white]{child}[/white]")
                add_children(child_node, child)
    
    add_children(tree, local_name)
    return tree

# class_uri = 's223:EnumerationKind-Substance'
# testing out with other enumerationkinds
class_uri = 's223:EnumerationKind'
graph = Graph()
parse_ttl_files_in_directory('../../s223/vocab', graph)

# Define the s223 namespace

results = get_subclass_hierarchy(graph, class_uri)

# Build the subclass hierarchy
tree = build_tree(graph, class_uri, results)

# Print the tree

print(tree)
# %%
