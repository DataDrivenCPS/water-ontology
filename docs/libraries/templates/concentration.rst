
concentration
#############

.. tabs::

    .. tab:: Turtle

        .. code:: turtle

           @prefix P: <urn:___param___#> .
           @prefix ns1: <http://data.ashrae.org/standard223#> .
           @prefix ns3: <http://qudt.org/schema/qudt/> .
           @prefix ns4: <http://qudt.org/vocab/quantitykind/> .
           
           P:name a ns1:QuantifiableObservableProperty ;
               ns1:ofSubstance P:substance ;
               ns3:hasQuantityKind ns4:Concentration ;
               ns3:hasUnit P:unit .
           
           

    .. tab:: With Inline Dependencies

        .. code:: turtle

            @prefix P: <urn:___param___#> .
            @prefix ns1: <http://qudt.org/schema/qudt/> .
            @prefix ns2: <http://data.ashrae.org/standard223#> .

            P:name a ns2:QuantifiableObservableProperty ;
                ns2:ofSubstance P:substance ;
                ns1:hasQuantityKind <http://qudt.org/vocab/quantitykind/Concentration> ;
                ns1:hasUnit P:unit .



Parameters
----------

- name
- unit
- substance


Dependencies
------------



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
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns3:hasQuantityKind</font> >];
            node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:ofSubstance</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>ns3:hasUnit</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableObservableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableObservableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableObservableProperty</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Concentration</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/Concentration' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/Concentration</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>substance</B></td></tr><tr><td href='urn:___param___#substance' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#substance</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>unit</B></td></tr><tr><td href='urn:___param___#unit' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#unit</font></td></tr></table> >];
            }
            

    .. tab:: With Inline Dependencies

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns2:ofSubstance</font> >];
            node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasUnit</font> >];
            node0 -> node4 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Concentration</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/Concentration' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/Concentration</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>substance</B></td></tr><tr><td href='urn:___param___#substance' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#substance</font></td></tr></table> >];
            node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>unit</B></td></tr><tr><td href='urn:___param___#unit' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#unit</font></td></tr></table> >];
            node4 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableObservableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableObservableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableObservableProperty</font></td></tr></table> >];
            }
            
