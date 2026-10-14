cl2-mgL
========

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
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a s223:QuantifiableObservableProperty ;
        s223:ofSubstance watr:Constituent-ChlorineResidual ;
        qudt:hasQuantityKind quantitykind:Concentration ;
        qudt:hasUnit unit:MilliGM-PER-L .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix unit: <http://qudt.org/vocab/unit/> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a s223:QuantifiableObservableProperty ;
        s223:ofSubstance watr:Constituent-ChlorineResidual ;
        qudt:hasQuantityKind quantitykind:Concentration ;
        qudt:hasUnit unit:MilliGM-PER-L .


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
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:ofSubstance</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasQuantityKind</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasUnit</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#Constituent-ChlorineResidual node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-ChlorineResidual</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#Constituent-ChlorineResidual' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#Constituent-ChlorineResidual</font></td></tr></table> > ]
    # http://qudt.org/vocab/quantitykind/Concentration node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Concentration</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/Concentration' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/Concentration</font></td></tr></table> > ]
    # http://qudt.org/vocab/unit/MilliGM-PER-L node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MilliGM-PER-L</B></td></tr><tr><td href='http://qudt.org/vocab/unit/MilliGM-PER-L' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/MilliGM-PER-L</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#QuantifiableObservableProperty node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableObservableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableObservableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableObservableProperty</font></td></tr></table> > ]
    }
