
pump-with-vfd
#############

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns2: <urn:nawi-water-ontology#> .
    @prefix ns3: <urn:___param___#> .
    
    ns3:name a ns2:Pump ;
        ns1:contains ns3:pump-name,
            ns3:vfd-name ;
        ns1:hasConnectionPoint ns3:elec-in,
            ns3:in,
            ns3:out ;
        ns1:hasProperty ns3:on-off-command,
            ns3:speed-command .
    
    ns3:pump-in ns1:mapsTo ns3:in .
    
    ns3:pump-out ns1:mapsTo ns3:out .
    
    ns3:vfd-in ns1:mapsTo ns3:elec-in .
    
    ns3:vfd-out ns1:cnx ns3:pump-elec-in .
    
    ns3:vfd-name ns1:connectsTo ns3:pump-name ;
        ns1:mapsTo ns3:elec-in .
    
    ns3:pump-name ns1:cnx ns3:pump-elec-in ;
        ns1:hasConnectionPoint ns3:pump-elec-in ;
        ns1:hasMedium ns3:elec-medium .
    
    

Parameters
----------

- pump-name
- elec-in
- vfd-in
- pump-elec-in
- elec-medium
- pump-in
- on-off-command
- out
- vfd-out
- speed-command
- name
- vfd-name
- in
- pump-out

Dependencies
------------

- :doc:`on-off-command`
- :doc:`speed-command`
- :doc:`inlet-cp`
- :doc:`inlet-cp`
- :doc:`outlet-cp`
- :doc:`pump`
- :doc:`vfd`


Backlinks
---------

No templates depend on this template.

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node6 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:connectsTo</font> >];
    node4 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
    node0 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node9 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node0 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
    node12 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
    node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
    node0 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node13 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node0 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
    node6 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node0 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
    node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
    node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Pump</B></td></tr><tr><td href='urn:nawi-water-ontology#Pump' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Pump</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-in</B></td></tr><tr><td href='urn:___param___#vfd-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-in</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in</B></td></tr><tr><td href='urn:___param___#elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in</font></td></tr></table> >];
    node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name</B></td></tr><tr><td href='urn:___param___#pump-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name</font></td></tr></table> >];
    node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-elec-in</B></td></tr><tr><td href='urn:___param___#pump-elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-elec-in</font></td></tr></table> >];
    node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name</B></td></tr><tr><td href='urn:___param___#vfd-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name</font></td></tr></table> >];
    node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-medium</B></td></tr><tr><td href='urn:___param___#elec-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-medium</font></td></tr></table> >];
    node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
    node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-in</B></td></tr><tr><td href='urn:___param___#pump-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-in</font></td></tr></table> >];
    node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
    node11 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>on-off-command</B></td></tr><tr><td href='urn:___param___#on-off-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#on-off-command</font></td></tr></table> >];
    node12 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-out</B></td></tr><tr><td href='urn:___param___#vfd-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-out</font></td></tr></table> >];
    node13 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-out</B></td></tr><tr><td href='urn:___param___#pump-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-out</font></td></tr></table> >];
    node14 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>speed-command</B></td></tr><tr><td href='urn:___param___#speed-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#speed-command</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node5 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node7 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasUnit</font> >];
        node9 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node11 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node13 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node15 -> node16 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node17 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
        node18 -> node19 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node2 -> node0 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node5 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node21 -> node13 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
        node22 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node17 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node21 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node22 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node22 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node23 -> node24 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node23 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node4 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node0 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node17 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node26 -> node27 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node23 -> node28 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node1 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node13 -> node17 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node15 -> node29 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasEnumerationKind</font> >];
        node21 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
        node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
        node30 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node13 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:connectsTo</font> >];
        node31 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node21 -> node32 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node21 -> node26 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node24 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node11 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node24 -> node28 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node18 -> node30 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node13 -> node33 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
        node13 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node9 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node31 -> node27 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node26 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node22 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node2 -> node34 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node13 -> node22 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node30 -> node19 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node18 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node2 -> node35 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
        node0 -> node18 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node21 -> node15 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
        node4 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node2 -> node32 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node26 -> node31 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node7 -> node36 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasQuantityKind</font> >];
        node17 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node21 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
        node21 -> node18 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node2 -> node23 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
        node23 -> node26 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node0 -> node37 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node7 -> node38 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node1 -> node37 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-in</B></td></tr><tr><td href='urn:___param___#pump-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-in</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-in-mapsto</B></td></tr><tr><td href='urn:___param___#pump-name-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-in-mapsto</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name</B></td></tr><tr><td href='urn:___param___#pump-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-elec-in</B></td></tr><tr><td href='urn:___param___#pump-elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-elec-in</font></td></tr></table> >];
        node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in</B></td></tr><tr><td href='urn:___param___#elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in</font></td></tr></table> >];
        node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in-mapsto</B></td></tr><tr><td href='urn:___param___#elec-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in-mapsto</font></td></tr></table> >];
        node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in-medium</B></td></tr><tr><td href='urn:___param___#elec-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in-medium</font></td></tr></table> >];
        node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>speed-command</B></td></tr><tr><td href='urn:___param___#speed-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#speed-command</font></td></tr></table> >];
        node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PERCENT</font></td></tr></table> >];
        node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-out-mapsto</B></td></tr><tr><td href='urn:___param___#vfd-name-out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-out-mapsto</font></td></tr></table> >];
        node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-out-medium</B></td></tr><tr><td href='urn:___param___#vfd-name-out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-out-medium</font></td></tr></table> >];
        node11 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-in-mapsto</B></td></tr><tr><td href='urn:___param___#vfd-name-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-in-mapsto</font></td></tr></table> >];
        node12 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-in-medium</B></td></tr><tr><td href='urn:___param___#vfd-name-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-in-medium</font></td></tr></table> >];
        node13 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name</B></td></tr><tr><td href='urn:___param___#vfd-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name</font></td></tr></table> >];
        node14 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>VariableFrequencyDrive</B></td></tr><tr><td href='urn:nawi-water-ontology#VariableFrequencyDrive' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#VariableFrequencyDrive</font></td></tr></table> >];
        node15 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>on-off-command</B></td></tr><tr><td href='urn:___param___#on-off-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#on-off-command</font></td></tr></table> >];
        node16 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumeratedActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumeratedActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumeratedActuatableProperty</font></td></tr></table> >];
        node17 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-out</B></td></tr><tr><td href='urn:___param___#vfd-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-out</font></td></tr></table> >];
        node18 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
        node19 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-medium</B></td></tr><tr><td href='urn:___param___#in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-medium</font></td></tr></table> >];
        node20 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> >];
        node21 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node22 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-in</B></td></tr><tr><td href='urn:___param___#vfd-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-in</font></td></tr></table> >];
        node23 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-out</B></td></tr><tr><td href='urn:___param___#pump-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-out</font></td></tr></table> >];
        node24 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-out-mapsto</B></td></tr><tr><td href='urn:___param___#pump-name-out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-out-mapsto</font></td></tr></table> >];
        node25 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>OutletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#OutletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#OutletConnectionPoint</font></td></tr></table> >];
        node26 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
        node27 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-medium</B></td></tr><tr><td href='urn:___param___#out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-medium</font></td></tr></table> >];
        node28 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-out-medium</B></td></tr><tr><td href='urn:___param___#pump-name-out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-out-medium</font></td></tr></table> >];
        node29 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumerationKind-OnOff</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumerationKind-OnOff' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumerationKind-OnOff</font></td></tr></table> >];
        node30 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-mapsto</B></td></tr><tr><td href='urn:___param___#in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-mapsto</font></td></tr></table> >];
        node31 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-mapsto</B></td></tr><tr><td href='urn:___param___#out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-mapsto</font></td></tr></table> >];
        node32 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Pump</B></td></tr><tr><td href='urn:nawi-water-ontology#Pump' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Pump</font></td></tr></table> >];
        node33 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-role</B></td></tr><tr><td href='urn:___param___#vfd-name-role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-role</font></td></tr></table> >];
        node34 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-medium</B></td></tr><tr><td href='urn:___param___#elec-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-medium</font></td></tr></table> >];
        node35 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-role</B></td></tr><tr><td href='urn:___param___#pump-name-role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-role</font></td></tr></table> >];
        node36 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>SpeedRatio</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/SpeedRatio' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/SpeedRatio</font></td></tr></table> >];
        node37 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-in-medium</B></td></tr><tr><td href='urn:___param___#pump-name-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-in-medium</font></td></tr></table> >];
        node38 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableActuatableProperty</font></td></tr></table> >];
        }
        
