water-flow
==========

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix unit: <http://qudt.org/vocab/unit/> .

    P:name a s223:QuantifiableObservableProperty ;
        s223:ofMedium s223:Fluid-Water ;
        qudt:hasQuantityKind quantitykind:VolumeFlowRate ;
        qudt:hasUnit unit:FT3-PER-MIN .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix unit: <http://qudt.org/vocab/unit/> .

    P:name-owner s223:hasProperty P:name .

    P:name a s223:Property,
            s223:QuantifiableObservableProperty ;
        s223:ofMedium s223:Fluid-Water ;
        qudt:hasQuantityKind quantitykind:VolumeFlowRate ;
        qudt:hasUnit unit:FT3-PER-MIN .


Parameters
----------

- ``name``
- ``name-owner``

Dependencies
------------

- :doc:`property`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:ofMedium</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasQuantityKind</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasUnit</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Fluid-Water node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Fluid-Water</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Fluid-Water' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Fluid-Water</font></td></tr></table> > ]
    # http://qudt.org/vocab/quantitykind/VolumeFlowRate node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>VolumeFlowRate</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/VolumeFlowRate' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/VolumeFlowRate</font></td></tr></table> > ]
    # http://qudt.org/vocab/unit/FT3-PER-MIN node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>FT3-PER-MIN</B></td></tr><tr><td href='http://qudt.org/vocab/unit/FT3-PER-MIN' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/FT3-PER-MIN</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#QuantifiableObservableProperty node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableObservableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableObservableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableObservableProperty</font></td></tr></table> > ]
    }
