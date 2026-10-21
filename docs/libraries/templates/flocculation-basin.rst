flocculation-basin
==================

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

    P:name a watr:FlocculationBasin ;
        rdfs:label P:label ;
        s223:cnx P:drain,
            P:in,
            P:out,
            P:overflow ;
        s223:hasConnectionPoint P:drain,
            P:in,
            P:out,
            P:overflow ;
        s223:hasRole P:role .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a watr:FlocculationBasin ;
        rdfs:label P:label ;
        s223:cnx P:drain,
            P:in,
            P:out,
            P:overflow ;
        s223:hasConnectionPoint P:drain,
            P:in,
            P:out,
            P:overflow ;
        s223:hasRole P:role .

    P:drain-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:drain-medium .

    P:in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium .

    P:out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium .

    P:overflow-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:overflow-medium .

    P:drain a s223:OutletConnectionPoint ;
        s223:hasMedium P:drain-medium ;
        s223:mapsTo P:drain-mapsto .

    P:in a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium ;
        s223:mapsTo P:in-mapsto .

    P:out a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium ;
        s223:mapsTo P:out-mapsto .

    P:overflow a s223:OutletConnectionPoint ;
        s223:hasMedium P:overflow-medium ;
        s223:mapsTo P:overflow-mapsto .


Parameters
----------

- ``drain``
- ``drain-mapsto``
- ``drain-medium``
- ``in``
- ``in-mapsto``
- ``in-medium``
- ``label``
- ``name``
- ``out``
- ``out-mapsto``
- ``out-medium``
- ``overflow``
- ``overflow-mapsto``
- ``overflow-medium``
- ``role``

Dependencies
------------

- :doc:`inlet-cp`
- :doc:`outlet-cp`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasRole</font> > ] ;
        node0 -> node6 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#drain node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>drain</B></td></tr><tr><td href='urn:___param___#drain' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#drain</font></td></tr></table> > ]
    # urn:___param___#in node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> > ]
    # urn:___param___#out node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> > ]
    # urn:___param___#overflow node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>overflow</B></td></tr><tr><td href='urn:___param___#overflow' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#overflow</font></td></tr></table> > ]
    # urn:___param___#role node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#FlocculationBasin node6
    node6 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>FlocculationBasin</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#FlocculationBasin' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#FlocculationBasin</font></td></tr></table> > ]
    }
