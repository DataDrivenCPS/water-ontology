property
========

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:owner s223:hasProperty P:name .

    P:name a s223:Property .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:owner s223:hasProperty P:name .

    P:name a s223:Property .


Parameters
----------

- ``name``
- ``owner``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node2 -> node0 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasProperty</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Property node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Property</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Property' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Property</font></td></tr></table> > ]
    # urn:___param___#owner node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>owner</B></td></tr><tr><td href='urn:___param___#owner' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#owner</font></td></tr></table> > ]
    }
