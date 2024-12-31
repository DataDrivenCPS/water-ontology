
ph
##

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns3: <urn:___param___#> .
    @prefix ns4: <http://qudt.org/schema/qudt/> .
    @prefix ns5: <http://qudt.org/vocab/quantitykind/> .
    
    ns3:name a ns1:QuantifiableObservableProperty ;
        ns4:hasQuantityKind ns5:Acidity ;
        ns4:unit <http://qudt.org/vocab/unit/PH> .
    
    

Parameters
----------

- name

Dependencies
------------



Backlinks
---------

No templates depend on this template.

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns4:hasQuantityKind</font> >];
    node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns4:unit</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableObservableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableObservableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableObservableProperty</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Acidity</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/Acidity' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/Acidity</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PH</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PH' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PH</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
        node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:unit</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableObservableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableObservableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableObservableProperty</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Acidity</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/Acidity' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/Acidity</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PH</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PH' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PH</font></td></tr></table> >];
        }
        
