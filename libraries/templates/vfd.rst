
vfd
###

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns2: <urn:nawi-water-ontology#> .
    @prefix ns3: <urn:___param___#> .
    
    ns3:name a ns2:VariableFrequencyDrive ;
        ns1:hasConnectionPoint ns3:in,
            ns3:out ;
        ns1:hasRole ns3:role .
    
    

Parameters
----------

- name
- role
- out
- in

Dependencies
------------

- :doc:`inlet-cp`
- :doc:`outlet-cp`


Backlinks
---------

- :doc:`pump-with-vfd`

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
    node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>VariableFrequencyDrive</B></td></tr><tr><td href='urn:nawi-water-ontology#VariableFrequencyDrive' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#VariableFrequencyDrive</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
    node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
        node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node0 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node2 -> node0 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node6 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node5 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node2 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node6 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node0 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node5 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node4 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node4 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node2 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-medium</B></td></tr><tr><td href='urn:___param___#in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-medium</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> >];
        node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
        node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-mapsto</B></td></tr><tr><td href='urn:___param___#out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-mapsto</font></td></tr></table> >];
        node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-mapsto</B></td></tr><tr><td href='urn:___param___#in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-mapsto</font></td></tr></table> >];
        node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> >];
        node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>OutletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#OutletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#OutletConnectionPoint</font></td></tr></table> >];
        node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-medium</B></td></tr><tr><td href='urn:___param___#out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-medium</font></td></tr></table> >];
        node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>VariableFrequencyDrive</B></td></tr><tr><td href='urn:nawi-water-ontology#VariableFrequencyDrive' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#VariableFrequencyDrive</font></td></tr></table> >];
        }
        
