import pandas as pd
from rdflib import Graph
import pyshacl


def get_prefixes(g: Graph):
    return "\n".join(f"PREFIX {prefix}: <{namespace}>" for prefix, namespace in g.namespace_manager.namespaces())

def convert_to_prefixed(uri, g: Graph):
    try:
        prefix, uri_ref, local_name = g.compute_qname(uri)
        return f"{prefix}:{local_name}"
    except Exception as e:
        print(e)
        return uri

def query_to_df(query, g: Graph):
    results = g.query(query)
    formatted_results = [
        [convert_to_prefixed(value, g) if isinstance(value, (str, bytes)) and value.startswith("http") else str(value) for value in row]
        for row in results
    ]
    df = pd.DataFrame(formatted_results, columns=[str(var) for var in results.vars])
    return df

import os

def parse_ttl_files_in_directory(directory_path, g):
    # Iterate through all files in the directory
    for file_name in os.listdir(directory_path):
        # Process only .ttl files
        if file_name.endswith(".ttl"):
            file_path = os.path.join(directory_path, file_name)
            print(f"Processing file: {file_name}")
            # Parse the .ttl file
            try:
                g.parse(file_path, format="turtle")
                # print(f"Parsed {len(g)} triples from {file_name}")
                
            except Exception as e:
                print(f"Error parsing {file_name}: {e}")
