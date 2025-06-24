
# Flow Graphs for Optimal Sensor Placement

To determine the **optimal locations for sensor placement** in a water treatment plant, we aim to monitor all water flows using the **fewest number of sensors**. This is achieved by constructing a **flow graph**, where:

**Nodes** represent system components (e.g., devices, junctions).

**Edges** represent water flows between these components.

We generate this graph from an RDF-based model of the plant. The graph abstraction implemented here is based on WWTP1, described in the paper "Optimal flow sensor placement on wastewater treatment plants" by Villez et al. (2016). We can identify a **minimal set of sensor placements** that covers all flows in the system.

## Ensuring Graph Completeness

To make the graph **fully closed** (i.e., all flows are accounted for), we introduce a special node called **`Environment`**, which represents everything external to the system. This step:

Connects all **inflows** and **outflows** to a common endpoint.
Prevents unconnected “open ends” where water appears or disappears.
Enforces **conservation** throughout the graph.

## Graph Construction Using SPARQL Rules

We use **SPARQL queries** to extract the necessary structure from the RDF model and simplify it into a usable flow graph. These rules:

Identify connections between devices and pipes.
Bypass non-essential intermediary nodes.
Attach unconnected flow endpoints to the `Environment`.



### Rule 1: Pipe Rule

Simplifies the topology by **removing intermediate connection points** and **directly links functional components**.

<pre>sparql
PREFIX s223: <http://data.ashrae.org/standard223#>

SELECT ?from ?conn ?to WHERE {
    ?conn s223:connectsFrom ?from .
    ?conn s223:connectsTo ?to .
}
</pre>

### Rule 2: Environment Rule

Links **unconnected inlets and outlets** to the `Environment` node while preserving **flow directionality**.

<pre>sparql
PREFIX s223: <http://data.ashrae.org/standard223#>

SELECT ?from ?conn ?to WHERE {
    {
        ?to_orig rdf:type s223:OutletConnectionPoint .
        ?from s223:hasConnectionPoint ?to_orig .
        FILTER NOT EXISTS {
            ?to_orig s223:connectsThrough ?conn_orig
        }
        BIND("connects_to_env" AS ?conn)
        BIND("Environment" AS ?to)
    }
    UNION 
    {
        ?from_orig rdf:type s223:InletConnectionPoint .
        ?to s223:hasConnectionPoint ?from_orig .
        FILTER NOT EXISTS {
            ?from_orig s223:connectsThrough ?conn_orig
        }
        BIND("connects_to_env" AS ?conn)
        BIND("Environment" AS ?from)
    }
}
</pre>

## Running the System

### Setup Instructions

1. **Install Poetry** (if not already installed):
   ```bash
   pip install poetry
   ```

2. **Generate the RDF Model**:
   Run one of the model scripts:
   ```bash
   python kv1.py
   # or
   python kv2.py
   ```

3. **Extract the Flow Graph Topology**:
   Use Poetry to run the extraction script:
   ```bash
   poetry run python extract_topology.py
   ```

   This will output a simplified RDF graph ready for sensor placement optimization.
