
membrane-module
###############

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns2: <urn:nawi-water-ontology#> .
    @prefix ns3: <urn:___param___#> .
    
    ns3:membrane-in ns1:mapsTo ns3:in .
    
    ns3:membrane-out ns1:mapsTo ns3:out .
    
    ns3:name a ns2:Equipment ;
        ns1:contains ns3:membrane ;
        ns1:hasConnectionPoint ns3:in,
            ns3:out ;
        ns1:hasRole ns3:role .
    
    

Parameters
----------

- role
- out
- membrane
- membrane-in
- name
- in
- membrane-out

Dependencies
------------

- :doc:`inlet-cp`
- :doc:`outlet-cp`
- :doc:`membrane`


Backlinks
---------

No templates depend on this template.

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
    node3 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
    node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node6 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node0 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Equipment</B></td></tr><tr><td href='urn:nawi-water-ontology#Equipment' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Equipment</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-in</B></td></tr><tr><td href='urn:___param___#membrane-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-in</font></td></tr></table> >];
    node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
    node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane</B></td></tr><tr><td href='urn:___param___#membrane' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane</font></td></tr></table> >];
    node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-out</B></td></tr><tr><td href='urn:___param___#membrane-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-out</font></td></tr></table> >];
    node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
        node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node6 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node8 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node9 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node6 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node11 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node2 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node11 -> node13 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node14 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 -> node15 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node6 -> node16 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node6 -> node17 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node4 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node7 -> node18 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node0 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node14 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node11 -> node19 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
        node7 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node4 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node14 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node11 -> node0 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
        node16 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node11 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node16 -> node17 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node4 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node9 -> node18 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node8 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node7 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane</B></td></tr><tr><td href='urn:___param___#membrane' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-role</B></td></tr><tr><td href='urn:___param___#membrane-role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-role</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-mapsto</B></td></tr><tr><td href='urn:___param___#in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-mapsto</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> >];
        node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-in</B></td></tr><tr><td href='urn:___param___#membrane-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-in</font></td></tr></table> >];
        node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-in-medium</B></td></tr><tr><td href='urn:___param___#membrane-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-in-medium</font></td></tr></table> >];
        node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-out</B></td></tr><tr><td href='urn:___param___#membrane-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-out</font></td></tr></table> >];
        node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
        node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-in-mapsto</B></td></tr><tr><td href='urn:___param___#membrane-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-in-mapsto</font></td></tr></table> >];
        node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-mapsto</B></td></tr><tr><td href='urn:___param___#out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-mapsto</font></td></tr></table> >];
        node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>OutletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#OutletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#OutletConnectionPoint</font></td></tr></table> >];
        node11 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node12 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-medium</B></td></tr><tr><td href='urn:___param___#in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-medium</font></td></tr></table> >];
        node13 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Equipment</B></td></tr><tr><td href='urn:nawi-water-ontology#Equipment' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Equipment</font></td></tr></table> >];
        node14 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
        node15 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Membrane</B></td></tr><tr><td href='urn:nawi-water-ontology#Membrane' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Membrane</font></td></tr></table> >];
        node16 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-out-mapsto</B></td></tr><tr><td href='urn:___param___#membrane-out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-out-mapsto</font></td></tr></table> >];
        node17 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-out-medium</B></td></tr><tr><td href='urn:___param___#membrane-out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-out-medium</font></td></tr></table> >];
        node18 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-medium</B></td></tr><tr><td href='urn:___param___#out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-medium</font></td></tr></table> >];
        node19 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> >];
        }
        
