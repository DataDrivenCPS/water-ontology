membrane-module
===============

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:membrane-in s223:mapsTo P:in .

    P:membrane-out s223:mapsTo P:out .

    P:name a s223:Equipment ;
        rdfs:label P:label ;
        s223:contains P:membrane ;
        s223:hasConnectionPoint P:in,
            P:out ;
        s223:hasRole P:role .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a s223:Equipment ;
        rdfs:label P:label ;
        s223:contains P:membrane ;
        s223:hasConnectionPoint P:in,
            P:out ;
        s223:hasRole P:role .

    P:in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium .

    P:membrane a s223:Equipment ;
        rdfs:label P:membrane-label ;
        s223:hasConnectionPoint P:membrane-in,
            P:membrane-out ;
        s223:hasRole P:membrane-role ;
        watr:hasProcess watr:Process-MembraneProcess .

    P:membrane-in a s223:InletConnectionPoint ;
        s223:hasMedium P:membrane-in-medium ;
        s223:mapsTo P:in,
            P:membrane-in-mapsto .

    P:membrane-in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:membrane-in-medium .

    P:membrane-out a s223:OutletConnectionPoint ;
        s223:hasMedium P:membrane-out-medium ;
        s223:mapsTo P:membrane-out-mapsto,
            P:out .

    P:membrane-out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:membrane-out-medium .

    P:out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium .

    P:in a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium ;
        s223:mapsTo P:in-mapsto .

    P:out a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium ;
        s223:mapsTo P:out-mapsto .


Parameters
----------

- ``in``
- ``in-mapsto``
- ``in-medium``
- ``label``
- ``membrane``
- ``membrane-in``
- ``membrane-in-mapsto``
- ``membrane-in-medium``
- ``membrane-label``
- ``membrane-out``
- ``membrane-out-mapsto``
- ``membrane-out-medium``
- ``membrane-role``
- ``name``
- ``out``
- ``out-mapsto``
- ``out-medium``
- ``role``

Dependencies
------------

- :doc:`inlet-cp`
- :doc:`membrane`
- :doc:`outlet-cp`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node2 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node4 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:contains</font> > ] ;
        node4 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node4 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node4 -> node6 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasRole</font> > ] ;
        node4 -> node7 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#membrane-in node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-in</B></td></tr><tr><td href='urn:___param___#membrane-in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-in</font></td></tr></table> > ]
    # urn:___param___#in node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> > ]
    # urn:___param___#membrane-out node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane-out</B></td></tr><tr><td href='urn:___param___#membrane-out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane-out</font></td></tr></table> > ]
    # urn:___param___#out node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> > ]
    # urn:___param___#name node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#membrane node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>membrane</B></td></tr><tr><td href='urn:___param___#membrane' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#membrane</font></td></tr></table> > ]
    # urn:___param___#role node6
    node6 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Equipment node7
    node7 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Equipment</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Equipment' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Equipment</font></td></tr></table> > ]
    }
