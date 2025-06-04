
brine
#####

.. tabs::

    .. tab:: Turtle

        .. code:: turtle

           @prefix P: <urn:___param___#> .
           @prefix ns1: <http://data.ashrae.org/standard223#> .
           @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
           
           P:name a ns1:Class,
                   P:name ;
               rdfs:label "Brine-VariablePercent" ;
               ns1:composedOf P:salt-name,
                   P:water-name ;
               rdfs:subClassOf ns1:Fluid-Water,
                   <urn:nawi-water-ontology#Water-Brine> .
           
           

    .. tab:: With Inline Dependencies

        .. code:: turtle

            @prefix P: <urn:___param___#> .
            @prefix ns1: <http://data.ashrae.org/standard223#> .
            @prefix ns2: <http://qudt.org/schema/qudt/> .
            @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

            P:name a ns1:Class,
                    P:name ;
                rdfs:label "Brine-VariablePercent" ;
                ns1:composedOf P:salt-name,
                    P:water-name ;
                rdfs:subClassOf ns1:Fluid-Water,
                    <urn:nawi-water-ontology#Water-Brine> .

            P:salt-name a ns1:QuantifiableProperty ;
                ns1:hasQuantityKind <http://qudt.org/vocab/quantitykind/MassFraction> ;
                ns1:hasValue P:salt-value ;
                ns1:ofConstituent <urn:nawi-water-ontology#Constituent-NaCl> ;
                ns2:hasUnit ns2:PERCENT .

            P:water-name a ns1:QuantifiableProperty ;
                ns1:hasQuantityKind <http://qudt.org/vocab/quantitykind/MassFraction> ;
                ns1:hasValue P:water-value ;
                ns1:ofConstituent ns1:Constituent-H20 ;
                ns2:hasUnit ns2:PERCENT .



Parameters
----------

- salt-name is a :doc:`constituent-salt`
- salt-value is a :doc:`constituent-salt`
- water-name is a :doc:`constituent-water`
- water-value is a :doc:`constituent-water`
- name


Dependencies
------------

- :doc:`constituent-salt`
- :doc:`constituent-water`


Dependents
----------

Nothing depends on this template.

Graph Visualization
--------------------

.. tabs::

    .. tab:: Template

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node0 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>rdfs:subClassOf</font> >];
            node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:composedOf</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>rdfs:subClassOf</font> >];
            node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:composedOf</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Brine-VariablePercent</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Class</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Class' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Class</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Fluid-Water</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Fluid-Water' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Fluid-Water</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>salt-name</B></td></tr><tr><td href='urn:___param___#salt-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#salt-name</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Water-Brine</B></td></tr><tr><td href='urn:nawi-water-ontology#Water-Brine' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Water-Brine</font></td></tr></table> >];
            node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>water-name</B></td></tr><tr><td href='urn:___param___#water-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#water-name</font></td></tr></table> >];
            }
            

    .. tab:: With Inline Dependencies

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdfs:subClassOf</font> >];
            node0 -> node0 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>rdfs:subClassOf</font> >];
            node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node4 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
            node6 -> node7 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasValue</font> >];
            node6 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:composedOf</font> >];
            node4 -> node8 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasValue</font> >];
            node4 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node6 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:composedOf</font> >];
            node6 -> node10 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofConstituent</font> >];
            node6 -> node9 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node4 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasUnit</font> >];
            node4 -> node12 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofConstituent</font> >];
            node6 -> node11 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasUnit</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Brine-VariablePercent</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Fluid-Water</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Fluid-Water' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Fluid-Water</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Water-Brine</B></td></tr><tr><td href='urn:nawi-water-ontology#Water-Brine' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Water-Brine</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Class</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Class' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Class</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>water-name</B></td></tr><tr><td href='urn:___param___#water-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#water-name</font></td></tr></table> >];
            node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MassFraction</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/MassFraction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/MassFraction</font></td></tr></table> >];
            node6 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>salt-name</B></td></tr><tr><td href='urn:___param___#salt-name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#salt-name</font></td></tr></table> >];
            node7 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>salt-value</B></td></tr><tr><td href='urn:___param___#salt-value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#salt-value</font></td></tr></table> >];
            node8 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>water-value</B></td></tr><tr><td href='urn:___param___#water-value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#water-value</font></td></tr></table> >];
            node9 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> >];
            node10 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-NaCl</B></td></tr><tr><td href='urn:nawi-water-ontology#Constituent-NaCl' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Constituent-NaCl</font></td></tr></table> >];
            node11 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/schema/qudt/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/schema/qudt/PERCENT</font></td></tr></table> >];
            node12 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-H20</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Constituent-H20' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Constituent-H20</font></td></tr></table> >];
            }
            
