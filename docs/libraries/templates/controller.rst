controller
==========

Generated from ``libraries/templates`` by
``scripts/generate_template_docs.py``. Bind the ``P:`` parameters
before using these graph fragments as a plant model.

Template
--------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a watr:Controller ;
        rdfs:label P:label .


With dependencies
-----------------

.. code-block:: turtle

    @prefix P: <urn:___param___#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix watr: <https://watermetadata.org/ontology/watr#> .

    P:name a watr:Controller ;
        rdfs:label P:label .


Parameters
----------

- ``label``
- ``name``

Dependencies
------------

None.

Graph
-----

.. graphviz::

    digraph {
     node [ fontname="DejaVu Sans" ] ;
        node0 -> node1 [ color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> > ] ;
    # urn:___param___#name node0
    node0 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>urn:___param___#label</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> > ]
    # https://watermetadata.org/ontology/watr#Controller node1
    node1 [ shape=none, color=black label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Controller</B></td></tr><tr><td href='https://watermetadata.org/ontology/watr#Controller' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>https://watermetadata.org/ontology/watr#Controller</font></td></tr></table> > ]
    }
