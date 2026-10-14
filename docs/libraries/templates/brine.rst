brine
=====

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a s223:Class,
            P:name ;
        rdfs:label "Brine-VariablePercent" ;
        s223:composedOf P:salt-name,
            P:water-name ;
        rdfs:subClassOf s223:Fluid-Water,
            watr:Water-Brine .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix unit: <http://qudt.org/vocab/unit/> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a s223:Class,
            P:name ;
        rdfs:label "Brine-VariablePercent" ;
        s223:composedOf P:salt-name,
            P:water-name ;
        rdfs:subClassOf s223:Fluid-Water,
            watr:Water-Brine .

    P:salt-name a s223:QuantifiableProperty ;
        s223:hasValue P:salt-value ;
        s223:ofConstituent watr:Salt-NaCl ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT .

    P:water-name a s223:QuantifiableProperty ;
        s223:hasValue P:water-value ;
        s223:ofConstituent s223:Constituent-H2O ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT .


Parameters
----------

- ``name``
- ``salt-name``
- ``salt-value``
- ``water-name``
- ``water-value``

Dependencies
------------

- :doc:`constituent-salt`
- :doc:`constituent-water`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:composedOf</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:composedOf</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node0 -> node0 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdfs:subClassOf</font> > ] ;
        node0 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdfs:subClassOf</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Brine-VariablePercent</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#salt-name node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>salt-name</B></td></tr><tr><td href='urn:___param___#salt-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#salt-name</font></td></tr></table> > ]
    # urn:___param___#water-name node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>water-name</B></td></tr><tr><td href='urn:___param___#water-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#water-name</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Class node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Class</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Class' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Class</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#Fluid-Water node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Fluid-Water</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Fluid-Water' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Fluid-Water</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#Water-Brine node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Water-Brine</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#Water-Brine' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#Water-Brine</font></td></tr></table> > ]
    }
