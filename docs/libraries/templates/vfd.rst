vfd
========

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

    P:name a watr:VariableFrequencyDrive ;
        rdfs:label P:label ;
        s223:hasConnectionPoint P:in,
            P:out ;
        s223:hasRole P:role .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix s223: <http://data.ashrae.org/standard223#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a watr:VariableFrequencyDrive ;
        rdfs:label P:label ;
        s223:hasConnectionPoint P:in,
            P:out ;
        s223:hasRole P:role .

    P:in a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium ;
        s223:mapsTo P:in-mapsto .

    P:in-mapsto a s223:InletConnectionPoint ;
        s223:hasMedium P:in-medium .

    P:out a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium ;
        s223:mapsTo P:out-mapsto .

    P:out-mapsto a s223:OutletConnectionPoint ;
        s223:hasMedium P:out-medium .


Parameters
----------

- ``in``
- ``in-mapsto``
- ``in-medium``
- ``label``
- ``name``
- ``out``
- ``out-mapsto``
- ``out-medium``
- ``role``

Dependencies
------------

- :doc:`inlet-cp`
- :doc:`outlet-cp`

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node2 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasConnectionPoint</font> > ] ;
        node0 -> node3 [ color=BLACK, label=< <font point-size='10' color='#336633'>s223:hasRole</font> > ] ;
        node0 -> node4 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # urn:___param___#in node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>in</B></td></tr><tr><td href='urn:___param___#in' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#in</font></td></tr></table> > ]
    # urn:___param___#out node2
    node2 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>out</B></td></tr><tr><td href='urn:___param___#out' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#out</font></td></tr></table> > ]
    # urn:___param___#role node3
    node3 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>role</B></td></tr><tr><td href='urn:___param___#role' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#role</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#VariableFrequencyDrive node4
    node4 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>VariableFrequencyDrive</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#VariableFrequencyDrive' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#VariableFrequencyDrive</font></td></tr></table> > ]
    }
