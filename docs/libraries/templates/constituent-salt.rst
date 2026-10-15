constituent-salt
================

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

    P:name a s223:QuantifiableProperty ;
        s223:hasValue P:value ;
        s223:ofConstituent watr:Salt-NaCl ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
    @prefix qudt: <http://qudt.org/schema/qudt/> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix unit: <http://qudt.org/vocab/unit/> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a s223:QuantifiableProperty ;
        s223:hasValue P:value ;
        s223:ofConstituent watr:Salt-NaCl ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT .


Parameters
----------

- ``name``
- ``value``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasValue</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:ofConstituent</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasQuantityKind</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>qudt:hasUnit</font> > ] ;
        node0 -> node5 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#value node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>value</B></td></tr><tr><td href='urn:___param___#value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#value</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#Salt-NaCl node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Salt-NaCl</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#Salt-NaCl' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#Salt-NaCl</font></td></tr></table> > ]
    # http://qudt.org/vocab/quantitykind/MassFraction node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MassFraction</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/MassFraction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/MassFraction</font></td></tr></table> > ]
    # http://qudt.org/vocab/unit/PERCENT node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PERCENT</font></td></tr></table> > ]
    # http://data.ashrae.org/standard223#QuantifiableProperty node5
    node5 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> > ]
    }
