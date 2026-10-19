quantifiable-property
=====================

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:owner s223:hasProperty P:name .

    P:constituent a s223:EnumerationKind-Substance .

    P:name a s223:QuantifiableProperty ;
        s223:ofConstituent P:constituent ;
        qudt:hasUnit P:unit .

    P:unit a qudt:Unit .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:owner s223:hasProperty P:name .

    P:constituent a s223:EnumerationKind-Substance .

    P:name a s223:QuantifiableProperty ;
        s223:ofConstituent P:constituent ;
        qudt:hasUnit P:unit .

    P:unit a qudt:Unit .


Parameters
----------

- ``constituent``
- ``name``
- ``owner``
- ``unit``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node2 -> node0 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:ofConstituent</font> > ] ;
        node2 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasUnit</font> > ] ;
        node2 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node5 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasProperty</font> > ] ;
        node3 -> node6 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#constituent node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>constituent</B></td></tr><tr><td href='urn:___param___#constituent' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#constituent</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#EnumerationKind-Substance node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumerationKind-Substance</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumerationKind-Substance' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumerationKind-Substance</font></td></tr></table> > ]
    # urn:___param___#name node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#unit node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>unit</B></td></tr><tr><td href='urn:___param___#unit' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#unit</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#QuantifiableProperty node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> > ]
    # urn:___param___#owner node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>owner</B></td></tr><tr><td href='urn:___param___#owner' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#owner</font></td></tr></table> > ]
    # http://qudt.org/schema/qudt/Unit node6
    node6 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Unit</B></td></tr><tr><td href='http://qudt.org/schema/qudt/Unit' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/schema/qudt/Unit</font></td></tr></table> > ]
    }
