pipe
====

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:Connection,
            s223:Pipe ;
        rdfs:label P:label ;
        s223:cnx P:destination,
            P:source .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:Connection,
            s223:Pipe ;
        rdfs:label P:label ;
        s223:cnx P:destination,
            P:source .


Parameters
----------

- ``destination``
- ``label``
- ``name``
- ``source``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:cnx</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#destination node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>destination</B></td></tr><tr><td href='urn:___param___#destination' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#destination</font></td></tr></table> > ]
    # urn:___param___#source node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>source</B></td></tr><tr><td href='urn:___param___#source' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#source</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Connection node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Connection</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Connection' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Connection</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Pipe node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Pipe</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Pipe' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Pipe</font></td></tr></table> > ]
    }
