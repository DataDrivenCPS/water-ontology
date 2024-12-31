
speed-command
#############

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns3: <urn:___param___#> .
    @prefix ns4: <http://qudt.org/schema/qudt/> .
    @prefix ns5: <http://qudt.org/vocab/quantitykind/> .
    @prefix ns6: <http://qudt.org/vocab/unit/> .
    
    ns3:name a ns1:QuantifiableActuatableProperty ;
        ns4:hasQuantityKind ns5:SpeedRatio ;
        ns4:hasUnit ns6:PERCENT .
    
    

Parameters
----------

- name

Dependencies
------------



Backlinks
---------

- :doc:`pump-with-vfd`

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns4:hasQuantityKind</font> >];
    node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns4:hasUnit</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableActuatableProperty</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>SpeedRatio</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/SpeedRatio' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/SpeedRatio</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PERCENT</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasQuantityKind</font> >];
        node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasUnit</font> >];
        node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>SpeedRatio</B></td></tr><tr><td href='http://qudt.org/vocab/quantitykind/SpeedRatio' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/quantitykind/SpeedRatio</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>PERCENT</B></td></tr><tr><td href='http://qudt.org/vocab/unit/PERCENT' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://qudt.org/vocab/unit/PERCENT</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>QuantifiableActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#QuantifiableActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#QuantifiableActuatableProperty</font></td></tr></table> >];
        }
        
