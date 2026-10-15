junction
========

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:Junction ;
        s223:cnx P:in,
            P:out ;
        s223:hasMedium P:medium .

    P:in a s223:InletConnectionPoint ;
        s223:hasMedium P:medium .

    P:out a s223:OutletConnectionPoint ;
        s223:hasMedium P:medium .

    P:medium a s223:Substance-Medium .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:Junction ;
        s223:cnx P:in,
            P:out ;
        s223:hasMedium P:medium .

    P:in a s223:InletConnectionPoint ;
        s223:hasMedium P:medium .

    P:out a s223:OutletConnectionPoint ;
        s223:hasMedium P:medium .

    P:medium a s223:Substance-Medium .


Parameters
----------

- ``in``
- ``medium``
- ``name``
- ``out``

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
        node1 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node4 -> node0 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node4 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node4 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasMedium</font> > ] ;
        node4 -> node6 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node5 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasMedium</font> > ] ;
        node5 -> node7 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#in node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> > ]
    # urn:___param___#medium node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>medium</B></td></tr><tr><td href='urn:___param___#medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#medium</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#InletConnectionPoint node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Substance-Medium node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Substance-Medium</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Substance-Medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Substance-Medium</font></td></tr></table> > ]
    # urn:___param___#name node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#out node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Junction node6
    node6 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Junction</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Junction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Junction</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#OutletConnectionPoint node7
    node7 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>OutletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#OutletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#OutletConnectionPoint</font></td></tr></table> > ]
    }
