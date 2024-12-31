
constituent-salt
################

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns2: <urn:nawi-water-ontology#> .
    @prefix ns3: <urn:___param___#> .
    @prefix ns4: <http://qudt.org/schema/qudt/> .
    
    ns3:name a ns1:QuantifiableProperty ;
        ns1:hasQuantityKind <http://qudt.org/vocab/quantitykind/MassFraction> ;
        ns1:hasValue ns3:value ;
        ns1:ofConstituent ns2:Constituent-NaCl ;
        ns4:hasUnit ns4:PERCENT .
    
    

Parameters
----------

- name
- value

Dependencies
------------



Backlinks
---------

- :doc:`brine`

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasValue</font> >];
    node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns4:hasUnit</font> >];
    node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
    node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofConstituent</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>value</B></td></tr><tr><td href='urn:___param___#value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#value</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/schema/qudt/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/schema/qudt/PERCENT</font></td></tr></table> >];
    node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MassFraction</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/MassFraction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/MassFraction</font></td></tr></table> >];
    node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-NaCl</B></td></tr><tr><td href='urn:nawi-water-ontology#Constituent-NaCl' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Constituent-NaCl</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasValue</font> >];
        node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasUnit</font> >];
        node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
        node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofConstituent</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>value</B></td></tr><tr><td href='urn:___param___#value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#value</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/schema/qudt/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/schema/qudt/PERCENT</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> >];
        node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MassFraction</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/MassFraction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/MassFraction</font></td></tr></table> >];
        node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-NaCl</B></td></tr><tr><td href='urn:nawi-water-ontology#Constituent-NaCl' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Constituent-NaCl</font></td></tr></table> >];
        }
        
