pump-with-vfd
=============

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a watr:Pump ;
        rdfs:label P:label ;
        s223:contains P:pump-name,
            P:vfd-name ;
        s223:hasConnectionPoint P:elec-in,
            P:in,
            P:out ;
        s223:hasProperty P:on-off-command,
            P:speed-command .

    P:pump-in s223:mapsTo P:in .

    P:pump-out s223:mapsTo P:out .

    P:vfd-in s223:mapsTo P:elec-in .

    P:vfd-out s223:cnx P:pump-elec-in .

    P:vfd-name s223:connectsTo P:pump-name ;
        s223:mapsTo P:elec-in .

    P:pump-name s223:cnx P:pump-elec-in ;
        s223:hasConnectionPoint P:pump-elec-in ;
        s223:hasMedium P:elec-medium .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix unit: <http://qudt.org/vocab/unit/> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a watr:Pump ;
        rdfs:label P:label ;
        s223:contains P:pump-name,
            P:vfd-name ;
        s223:hasConnectionPoint P:elec-in,
            P:in,
            P:out ;
        s223:hasProperty P:on-off-command,
            P:speed-command .

    P:elec-in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:elec-in-medium .

    P:in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium .

    P:on-off-command a s223:EnumeratedActuatableProperty ;
        s223:hasEnumerationKind s223:EnumerationKind-OnOff .

    P:out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium .

    P:pump-in a s223:InletConnectionPoint ;
        s223:hasMedium P:pump-name-in-medium ;
        s223:mapsTo P:in,
            P:pump-name-in-mapsto .

    P:pump-name-in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:pump-name-in-medium .

    P:pump-name-out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:pump-name-out-medium .

    P:pump-out a s223:OutletConnectionPoint ;
        s223:hasMedium P:pump-name-out-medium ;
        s223:mapsTo P:out,
            P:pump-name-out-mapsto .

    P:speed-command a s223:QuantifiableActuatableProperty ;
        qudt:hasQuantityKind quantitykind:SpeedRatio ;
        qudt:hasUnit unit:PERCENT .

    P:vfd-in a s223:InletConnectionPoint ;
        s223:hasMedium P:vfd-name-in-medium ;
        s223:mapsTo P:elec-in,
            P:vfd-name-in-mapsto .

    P:vfd-name a watr:VariableFrequencyDrive ;
        rdfs:label P:vfd-name-label ;
        s223:connectsTo P:pump-name ;
        s223:hasConnectionPoint P:vfd-in,
            P:vfd-out ;
        s223:hasRole P:vfd-name-role ;
        s223:mapsTo P:elec-in .

    P:vfd-name-in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:vfd-name-in-medium .

    P:vfd-name-out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:vfd-name-out-medium .

    P:vfd-out a s223:OutletConnectionPoint ;
        s223:cnx P:pump-elec-in ;
        s223:hasMedium P:vfd-name-out-medium ;
        s223:mapsTo P:vfd-name-out-mapsto .

    P:in a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium ;
        s223:mapsTo P:in-mapsto .

    P:out a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium ;
        s223:mapsTo P:out-mapsto .

    P:pump-name a watr:Pump ;
        rdfs:label P:pump-name-label ;
        s223:cnx P:pump-elec-in ;
        s223:hasConnectionPoint P:pump-elec-in,
            P:pump-in,
            P:pump-out ;
        s223:hasMedium P:elec-medium ;
        s223:hasRole P:pump-name-role .

    P:elec-in a s223:InletConnectionPoint ;
        s223:hasMedium P:elec-in-medium ;
        s223:mapsTo P:elec-in-mapsto .


Parameters
----------

- ``elec-in``
- ``elec-in-mapsto``
- ``elec-in-medium``
- ``elec-medium``
- ``in``
- ``in-mapsto``
- ``in-medium``
- ``label``
- ``name``
- ``on-off-command``
- ``out``
- ``out-mapsto``
- ``out-medium``
- ``pump-elec-in``
- ``pump-in``
- ``pump-name``
- ``pump-name-in-mapsto``
- ``pump-name-in-medium``
- ``pump-name-label``
- ``pump-name-out-mapsto``
- ``pump-name-out-medium``
- ``pump-name-role``
- ``pump-out``
- ``speed-command``
- ``vfd-in``
- ``vfd-name``
- ``vfd-name-in-mapsto``
- ``vfd-name-in-medium``
- ``vfd-name-label``
- ``vfd-name-out-mapsto``
- ``vfd-name-out-medium``
- ``vfd-name-role``
- ``vfd-out``

Dependencies
------------

- :doc:`inlet-cp`
- :doc:`on-off-command`
- :doc:`outlet-cp`
- :doc:`pump`
- :doc:`speed-command`
- :doc:`vfd`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:contains</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:contains</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node6 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasProperty</font> > ] ;
        node0 -> node7 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasProperty</font> > ] ;
        node0 -> node8 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node9 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node1 -> node10 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node1 -> node10 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node1 -> node11 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasMedium</font> > ] ;
        node12 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node13 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node2 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:connectsTo</font> > ] ;
        node2 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node14 -> node10 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#pump-name node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-name</B></td></tr><tr><td href='urn:___param___#pump-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-name</font></td></tr></table> > ]
    # urn:___param___#vfd-name node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-name</B></td></tr><tr><td href='urn:___param___#vfd-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-name</font></td></tr></table> > ]
    # urn:___param___#elec-in node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-in</B></td></tr><tr><td href='urn:___param___#elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-in</font></td></tr></table> > ]
    # urn:___param___#in node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> > ]
    # urn:___param___#out node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> > ]
    # urn:___param___#on-off-command node6
    node6 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>on-off-command</B></td></tr><tr><td href='urn:___param___#on-off-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#on-off-command</font></td></tr></table> > ]
    # urn:___param___#speed-command node7
    node7 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>speed-command</B></td></tr><tr><td href='urn:___param___#speed-command' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#speed-command</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#Pump node8
    node8 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Pump</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#Pump' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#Pump</font></td></tr></table> > ]
    # urn:___param___#pump-in node9
    node9 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-in</B></td></tr><tr><td href='urn:___param___#pump-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-in</font></td></tr></table> > ]
    # urn:___param___#pump-elec-in node10
    node10 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-elec-in</B></td></tr><tr><td href='urn:___param___#pump-elec-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-elec-in</font></td></tr></table> > ]
    # urn:___param___#elec-medium node11
    node11 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>elec-medium</B></td></tr><tr><td href='urn:___param___#elec-medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#elec-medium</font></td></tr></table> > ]
    # urn:___param___#pump-out node12
    node12 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>pump-out</B></td></tr><tr><td href='urn:___param___#pump-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#pump-out</font></td></tr></table> > ]
    # urn:___param___#vfd-in node13
    node13 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-in</B></td></tr><tr><td href='urn:___param___#vfd-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-in</font></td></tr></table> > ]
    # urn:___param___#vfd-out node14
    node14 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>vfd-out</B></td></tr><tr><td href='urn:___param___#vfd-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#vfd-out</font></td></tr></table> > ]
    }
