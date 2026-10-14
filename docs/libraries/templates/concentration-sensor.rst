concentration-sensor
====================

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:Sensor ;
        rdfs:label P:label ;
        s223:hasObservationLocation P:where ;
        s223:observes P:property .

    P:property s223:ofConstituent P:substance ;
        qudt:hasUnit P:unit .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .

    P:name a s223:Sensor ;
        rdfs:label P:label ;
        s223:hasObservationLocation P:where ;
        s223:observes P:property .

    P:property-owner s223:hasProperty P:property .

    P:substance a s223:EnumerationKind-Substance .

    P:unit a qudt:Unit .

    P:property a s223:QuantifiableProperty ;
        s223:ofConstituent P:substance ;
        qudt:hasUnit P:unit .


Parameters
----------

- ``label``
- ``name``
- ``property``
- ``property-owner``
- ``substance``
- ``unit``
- ``where``

Dependencies
------------

- :doc:`quantifiable-property`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasObservationLocation</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:observes</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node2 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:ofConstituent</font> > ] ;
        node2 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasUnit</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#where node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>where</B></td></tr><tr><td href='urn:___param___#where' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#where</font></td></tr></table> > ]
    # urn:___param___#property node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>property</B></td></tr><tr><td href='urn:___param___#property' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#property</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Sensor node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Sensor</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Sensor' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Sensor</font></td></tr></table> > ]
    # urn:___param___#substance node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>substance</B></td></tr><tr><td href='urn:___param___#substance' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#substance</font></td></tr></table> > ]
    # urn:___param___#unit node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>unit</B></td></tr><tr><td href='urn:___param___#unit' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#unit</font></td></tr></table> > ]
    }
