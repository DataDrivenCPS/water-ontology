
pump-with-vfd
#############

.. tabs::

    .. tab:: Turtle

        .. code:: turtle

           @prefix P: <urn:___param___#> .
           @prefix ns1: <http://data.ashrae.org/standard223#> .
           @prefix ns2: <urn:nawi-water-ontology#> .
           
           P:name a ns2:Pump ;
               ns1:contains P:pump-name,
                   P:vfd-name ;
               ns1:hasConnectionPoint P:elec-in,
                   P:in,
                   P:out ;
               ns1:hasProperty P:on-off-command,
                   P:speed-command .
           
           P:pump-in ns1:mapsTo P:in .
           
           P:pump-out ns1:mapsTo P:out .
           
           P:vfd-in ns1:mapsTo P:elec-in .
           
           P:vfd-out ns1:cnx P:pump-elec-in .
           
           P:vfd-name ns1:connectsTo P:pump-name ;
               ns1:mapsTo P:elec-in .
           
           P:pump-name ns1:cnx P:pump-elec-in ;
               ns1:hasConnectionPoint P:pump-elec-in ;
               ns1:hasMedium P:elec-medium .
           
           

    .. tab:: With Inline Dependencies

        .. code:: turtle

            @prefix P: <urn:___param___#> .
            @prefix ns1: <http://data.ashrae.org/standard223#> .
            @prefix ns2: <http://qudt.org/schema/qudt/> .

            P:name a <urn:nawi-water-ontology#Pump> ;
                ns1:contains P:pump-name,
                    P:vfd-name ;
                ns1:hasConnectionPoint P:elec-in,
                    P:in,
                    P:out ;
                ns1:hasProperty P:on-off-command,
                    P:speed-command .

            P:elec-in-mapsto a ns1:InletConnectionPoint ;
                ns1:hasMedium P:elec-in-medium .

            P:in-mapsto a ns1:InletConnectionPoint ;
                ns1:hasMedium P:in-medium .

            P:on-off-command a ns1:EnumeratedActuatableProperty ;
                ns1:hasEnumerationKind ns1:EnumerationKind-OnOff .

            P:out-mapsto a ns1:OutletConnectionPoint ;
                ns1:hasMedium P:out-medium .

            P:pump-in a ns1:InletConnectionPoint ;
                ns1:hasMedium P:pump-name-in-medium ;
                ns1:mapsTo P:in,
                    P:pump-name-in-mapsto .

            P:pump-name-in-mapsto a ns1:InletConnectionPoint ;
                ns1:hasMedium P:pump-name-in-medium .

            P:pump-name-out-mapsto a ns1:OutletConnectionPoint ;
                ns1:hasMedium P:pump-name-out-medium .

            P:pump-out a ns1:OutletConnectionPoint ;
                ns1:hasMedium P:pump-name-out-medium ;
                ns1:mapsTo P:out,
                    P:pump-name-out-mapsto .

            P:speed-command a ns1:QuantifiableActuatableProperty ;
                ns2:hasQuantityKind <http://qudt.org/vocab/quantitykind/SpeedRatio> ;
                ns2:hasUnit <http://qudt.org/vocab/unit/PERCENT> .

            P:vfd-in a ns1:InletConnectionPoint ;
                ns1:hasMedium P:vfd-name-in-medium ;
                ns1:mapsTo P:elec-in,
                    P:vfd-name-in-mapsto .

            P:vfd-name a <urn:nawi-water-ontology#VariableFrequencyDrive> ;
                ns1:connectsTo P:pump-name ;
                ns1:hasConnectionPoint P:vfd-in,
                    P:vfd-out ;
                ns1:hasRole P:vfd-name-role ;
                ns1:mapsTo P:elec-in .

            P:vfd-name-in-mapsto a ns1:InletConnectionPoint ;
                ns1:hasMedium P:vfd-name-in-medium .

            P:vfd-name-out-mapsto a ns1:OutletConnectionPoint ;
                ns1:hasMedium P:vfd-name-out-medium .

            P:vfd-out a ns1:OutletConnectionPoint ;
                ns1:cnx P:pump-elec-in ;
                ns1:hasMedium P:vfd-name-out-medium ;
                ns1:mapsTo P:vfd-name-out-mapsto .

            P:in a ns1:InletConnectionPoint ;
                ns1:hasMedium P:in-medium ;
                ns1:mapsTo P:in-mapsto .

            P:out a ns1:OutletConnectionPoint ;
                ns1:hasMedium P:out-medium ;
                ns1:mapsTo P:out-mapsto .

            P:pump-name a <urn:nawi-water-ontology#Pump> ;
                ns1:cnx P:pump-elec-in ;
                ns1:hasConnectionPoint P:pump-elec-in,
                    P:pump-in,
                    P:pump-out ;
                ns1:hasMedium P:elec-medium ;
                ns1:hasRole P:pump-name-role .

            P:elec-in a ns1:InletConnectionPoint ;
                ns1:hasMedium P:elec-in-medium ;
                ns1:mapsTo P:elec-in-mapsto .



Parameters
----------

- on-off-command is a :doc:`on-off-command`
- speed-command is a :doc:`speed-command`
- elec-in is a :doc:`inlet-cp`
- in is a :doc:`inlet-cp`
- out is a :doc:`outlet-cp`
- pump-in is a :doc:`pump`
- pump-name is a :doc:`pump`
- pump-out is a :doc:`pump`
- vfd-in is a :doc:`vfd`
- vfd-name is a :doc:`vfd`
- vfd-out is a :doc:`vfd`
- elec-medium
- name
- pump-elec-in


Dependencies
------------

- :doc:`inlet-cp`
- :doc:`on-off-command`
- :doc:`outlet-cp`
- :doc:`pump`
- :doc:`speed-command`
- :doc:`vfd`


Dependents
----------

Nothing depends on this template.

Graph Visualization
--------------------

.. tabs::

    .. tab:: Template

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
            node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
            node6 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:connectsTo</font> >];
            node0 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
            node7 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node0 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node0 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
            node10 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node0 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
            node6 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node2 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node13 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node14 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Pump</B></td></tr><tr><td href='urn:nawi-water-ontology#Pump' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Pump</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name</B></td></tr><tr><td href='urn:___param___#pump-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-elec-in</B></td></tr><tr><td href='urn:___param___#pump-elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-elec-in</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
            node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>on-off-command</B></td></tr><tr><td href='urn:___param___#on-off-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#on-off-command</font></td></tr></table> >];
            node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name</B></td></tr><tr><td href='urn:___param___#vfd-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name</font></td></tr></table> >];
            node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-in</B></td></tr><tr><td href='urn:___param___#vfd-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-in</font></td></tr></table> >];
            node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in</B></td></tr><tr><td href='urn:___param___#elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in</font></td></tr></table> >];
            node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
            node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-in</B></td></tr><tr><td href='urn:___param___#pump-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-in</font></td></tr></table> >];
            node11 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>speed-command</B></td></tr><tr><td href='urn:___param___#speed-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#speed-command</font></td></tr></table> >];
            node12 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-medium</B></td></tr><tr><td href='urn:___param___#elec-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-medium</font></td></tr></table> >];
            node13 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-out</B></td></tr><tr><td href='urn:___param___#pump-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-out</font></td></tr></table> >];
            node14 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-out</B></td></tr><tr><td href='urn:___param___#vfd-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-out</font></td></tr></table> >];
            }
            

    .. tab:: With Inline Dependencies

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node6 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasUnit</font> >];
            node0 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node9 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node10 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node4 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node2 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node12 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node13 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node15 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node16 -> node17 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node0 -> node18 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
            node15 -> node19 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node12 -> node16 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node0 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node21 -> node22 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node21 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node23 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
            node24 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node23 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node24 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node17 -> node26 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node8 -> node25 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node8 -> node23 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node12 -> node27 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
            node6 -> node28 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node2 -> node29 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node9 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:connectsTo</font> >];
            node10 -> node30 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node20 -> node15 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node29 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:contains</font> >];
            node4 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node21 -> node13 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node9 -> node31 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasRole</font> >];
            node32 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node2 -> node24 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node16 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node12 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node32 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node16 -> node26 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node0 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasProperty</font> >];
            node29 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node13 -> node22 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node4 -> node32 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node20 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node12 -> node33 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node16 -> node20 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node21 -> node34 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
            node12 -> node34 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node0 -> node24 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node20 -> node19 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node12 -> node34 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:cnx</font> >];
            node24 -> node30 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
            node9 -> node21 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasConnectionPoint</font> >];
            node17 -> node14 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node6 -> node35 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasQuantityKind</font> >];
            node18 -> node36 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node9 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
            node18 -> node37 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasEnumerationKind</font> >];
            node8 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node9 -> node38 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Pump</B></td></tr><tr><td href='urn:nawi-water-ontology#Pump' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Pump</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-in</B></td></tr><tr><td href='urn:___param___#pump-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-in</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-in</B></td></tr><tr><td href='urn:___param___#vfd-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-in</font></td></tr></table> >];
            node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-in-medium</B></td></tr><tr><td href='urn:___param___#vfd-name-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-in-medium</font></td></tr></table> >];
            node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>speed-command</B></td></tr><tr><td href='urn:___param___#speed-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#speed-command</font></td></tr></table> >];
            node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PERCENT</font></td></tr></table> >];
            node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in</B></td></tr><tr><td href='urn:___param___#elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in</font></td></tr></table> >];
            node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name</B></td></tr><tr><td href='urn:___param___#vfd-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name</font></td></tr></table> >];
            node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-mapsto</B></td></tr><tr><td href='urn:___param___#in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-mapsto</font></td></tr></table> >];
            node11 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-in-medium</B></td></tr><tr><td href='urn:___param___#pump-name-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-in-medium</font></td></tr></table> >];
            node12 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name</B></td></tr><tr><td href='urn:___param___#pump-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name</font></td></tr></table> >];
            node13 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-out-mapsto</B></td></tr><tr><td href='urn:___param___#vfd-name-out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-out-mapsto</font></td></tr></table> >];
            node14 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>OutletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#OutletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#OutletConnectionPoint</font></td></tr></table> >];
            node15 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-mapsto</B></td></tr><tr><td href='urn:___param___#out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-mapsto</font></td></tr></table> >];
            node16 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-out</B></td></tr><tr><td href='urn:___param___#pump-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-out</font></td></tr></table> >];
            node17 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-out-mapsto</B></td></tr><tr><td href='urn:___param___#pump-name-out-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-out-mapsto</font></td></tr></table> >];
            node18 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>on-off-command</B></td></tr><tr><td href='urn:___param___#on-off-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#on-off-command</font></td></tr></table> >];
            node19 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out-medium</B></td></tr><tr><td href='urn:___param___#out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out-medium</font></td></tr></table> >];
            node20 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> >];
            node21 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-out</B></td></tr><tr><td href='urn:___param___#vfd-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-out</font></td></tr></table> >];
            node22 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-out-medium</B></td></tr><tr><td href='urn:___param___#vfd-name-out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-out-medium</font></td></tr></table> >];
            node23 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in-mapsto</B></td></tr><tr><td href='urn:___param___#elec-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in-mapsto</font></td></tr></table> >];
            node24 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> >];
            node25 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in-medium</B></td></tr><tr><td href='urn:___param___#elec-in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in-medium</font></td></tr></table> >];
            node26 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-out-medium</B></td></tr><tr><td href='urn:___param___#pump-name-out-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-out-medium</font></td></tr></table> >];
            node27 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-role</B></td></tr><tr><td href='urn:___param___#pump-name-role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-role</font></td></tr></table> >];
            node28 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableActuatableProperty</font></td></tr></table> >];
            node29 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name-in-mapsto</B></td></tr><tr><td href='urn:___param___#pump-name-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name-in-mapsto</font></td></tr></table> >];
            node30 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in-medium</B></td></tr><tr><td href='urn:___param___#in-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in-medium</font></td></tr></table> >];
            node31 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-role</B></td></tr><tr><td href='urn:___param___#vfd-name-role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-role</font></td></tr></table> >];
            node32 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name-in-mapsto</B></td></tr><tr><td href='urn:___param___#vfd-name-in-mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name-in-mapsto</font></td></tr></table> >];
            node33 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-medium</B></td></tr><tr><td href='urn:___param___#elec-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-medium</font></td></tr></table> >];
            node34 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-elec-in</B></td></tr><tr><td href='urn:___param___#pump-elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-elec-in</font></td></tr></table> >];
            node35 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>SpeedRatio</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/SpeedRatio' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/SpeedRatio</font></td></tr></table> >];
            node36 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumeratedActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumeratedActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumeratedActuatableProperty</font></td></tr></table> >];
            node37 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumerationKind-OnOff</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumerationKind-OnOff' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumerationKind-OnOff</font></td></tr></table> >];
            node38 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>VariableFrequencyDrive</B></td></tr><tr><td href='urn:nawi-water-ontology#VariableFrequencyDrive' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#VariableFrequencyDrive</font></td></tr></table> >];
            }
            
