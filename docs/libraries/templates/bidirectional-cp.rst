bidirectional-cp
================

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:BidirectionalConnectionPoint ;
        s223:hasMedium P:medium ;
        s223:mapsTo P:mapsto .

    P:mapsto a s223:BidirectionalConnectionPoint ;
        s223:hasMedium P:medium .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:BidirectionalConnectionPoint ;
        s223:hasMedium P:medium ;
        s223:mapsTo P:mapsto .

    P:mapsto a s223:BidirectionalConnectionPoint ;
        s223:hasMedium P:medium .


Parameters
----------

- ``mapsto``
- ``medium``
- ``name``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasMedium</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node3 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasMedium</font> > ] ;
        node3 -> node0 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:mapsTo</font> > ] ;
        node3 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#mapsto node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>mapsto</B></td></tr><tr><td href='urn:___param___#mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#mapsto</font></td></tr></table> > ]
    # urn:___param___#medium node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>medium</B></td></tr><tr><td href='urn:___param___#medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#medium</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#BidirectionalConnectionPoint node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>BidirectionalConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#BidirectionalConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#BidirectionalConnectionPoint</font></td></tr></table> > ]
    # urn:___param___#name node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    }
