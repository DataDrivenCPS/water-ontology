
constituent-water
#################

.. tabs::

    .. tab:: Turtle

        .. code:: turtle

           @prefix P: <urn:___param___#> .
           @prefix ns1: <http://data.ashrae.org/standard223#> .
           @prefix ns3: <http://qudt.org/schema/qudt/> .
           @prefix ns4: <http://qudt.org/vocab/quantitykind/> .
           
           P:name a ns1:QuantifiableProperty ;
               ns1:hasQuantityKind ns4:MassFraction ;
               ns1:hasValue P:value ;
               ns1:ofConstituent ns1:Constituent-H20 ;
               ns3:hasUnit ns3:PERCENT .
           
           

    .. tab:: With Inline Dependencies

        .. code:: turtle

            @prefix P: <urn:___param___#> .
            @prefix ns1: <http://data.ashrae.org/standard223#> .
            @prefix ns2: <http://qudt.org/schema/qudt/> .

            P:name a ns1:QuantifiableProperty ;
                ns1:hasQuantityKind <http://qudt.org/vocab/quantitykind/MassFraction> ;
                ns1:hasValue P:value ;
                ns1:ofConstituent ns1:Constituent-H20 ;
                ns2:hasUnit ns2:PERCENT .



Parameters
----------

- name
- value


Dependencies
------------



Dependents
----------

- :doc:`brine`

Graph Visualization
--------------------

.. tabs::

    .. tab:: Template

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
            node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasValue</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns3:hasUnit</font> >];
            node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofConstituent</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MassFraction</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/MassFraction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/MassFraction</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>value</B></td></tr><tr><td href='urn:___param___#value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#value</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/schema/qudt/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/schema/qudt/PERCENT</font></td></tr></table> >];
            node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-H20</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Constituent-H20' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Constituent-H20</font></td></tr></table> >];
            }
            

    .. tab:: With Inline Dependencies

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasValue</font> >];
            node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:hasUnit</font> >];
            node0 -> node5 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofConstituent</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>MassFraction</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/MassFraction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/MassFraction</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>value</B></td></tr><tr><td href='urn:___param___#value' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#value</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableProperty</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/schema/qudt/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/schema/qudt/PERCENT</font></td></tr></table> >];
            node5 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Constituent-H20</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Constituent-H20' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Constituent-H20</font></td></tr></table> >];
            }
            
