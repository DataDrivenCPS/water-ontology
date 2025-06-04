#%%
from utils import parse_ttl_files_in_directory, query_to_df
from rdflib import Graph
import pyshacl
from rdflib import OWL, RDF, RDFS, SH, Graph, Namespace

g = Graph()
g.parse('substances.ttl', format = 'ttl')

sg = Graph()
sg.parse('substances.ttl', format = 'ttl')
parse_ttl_files_in_directory('../../s223/vocab', sg)
parse_ttl_files_in_directory('../../s223/models', sg)
parse_ttl_files_in_directory('../../s223/inference', sg)
parse_ttl_files_in_directory('../../s223/validation', sg)

# Disabling annoying rules 


valid, report_graph, report_text = pyshacl.validate(
    data_graph=g,
    shacl_graph=sg,
    advanced=True,
    js=True,
    allow_warnings=False,
    inplace=True,
    iterate_rules=True,
    )

# 'ex:Generator' in report_text
# print(report_text)

# find the prefix definitions so the select can find them
namespace_map = {}
for prefix, uriref in report_graph.namespaces():
    namespace_map[prefix] = Namespace(uriref)
if "sh" not in namespace_map:
    namespace_map["sh"] = SH

# find the validation results
# Currently filtering out info in qs
qs = """
    SELECT ?resultSeverity ?sourceShape ?resultMessage ?focusNode ?value
    WHERE {
        ?report rdf:type sh:ValidationReport .
        ?report sh:result ?result .
        ?result sh:focusNode ?focusNode .
        OPTIONAL { ?result sh:resultMessage ?resultMessage } .
        ?result sh:resultSeverity ?resultSeverity .
        ?result sh:sourceShape ?sourceShape .
        OPTIONAL { ?result sh:value ?value } .
        # FILTER(?resultSeverity = s223:g36).
        }
    """

# pretty colors
color_map = {SH.Violation: 33, SH.Info: 34, SH.Warning: 35}

# run the query, sort the results
results = sorted(report_graph.query(qs, initNs=namespace_map))

prev = None
for resultSeverity, sourceShape, resultMessage, focusNode, value in results:
    if sourceShape != prev:
        color = color_map[resultSeverity]
        if resultMessage:
            print(f"\x1b[{color}m{resultMessage}\x1b[0m")
        # else:
        print(f"\x1b[{color}m{sourceShape}\x1b[0m")
        prev = sourceShape
    print(f"    {focusNode}{' ' + value if value else ''}")


# %%

query_to_df(""" 
SELECT $this ?conc
        WHERE {
          $this s223:composedOf ?constituent .
          ?constituent s223:hasValue ?conc ;
            s223:ofConstituent s223:Salt-NaCl .
          FILTER(?conc < 3 || ?conc < 26) .
          }
  """, g)
# %%
