on-off-command
==============

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:EnumeratedActuatableProperty ;
        s223:hasEnumerationKind s223:Binary-OnOff .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:EnumeratedActuatableProperty ;
        s223:hasEnumerationKind s223:Binary-OnOff .


Parameters
----------

- ``name``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasEnumerationKind</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Binary-OnOff node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Binary-OnOff</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Binary-OnOff' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Binary-OnOff</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#EnumeratedActuatableProperty node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumeratedActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumeratedActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumeratedActuatableProperty</font></td></tr></table> > ]
    }
