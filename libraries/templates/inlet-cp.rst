
inlet-cp
########

.. code-block:: turtle

    @prefix ns1: <http://data.ashrae.org/standard223#> .
    @prefix ns3: <urn:___param___#> .
    
    ns3:name a ns1:InletConnectionPoint ;
        ns1:hasMedium ns3:medium ;
        ns1:mapsTo ns3:mapsto .
    
    ns3:mapsto a ns1:InletConnectionPoint ;
        ns1:hasMedium ns3:medium .
    
    

Parameters
----------

- name
- mapsto
- medium

Dependencies
------------



Backlinks
---------

- :doc:`tank`
- :doc:`bladder`
- :doc:`valve`
- :doc:`filter`
- :doc:`membrane`
- :doc:`membrane-module`
- :doc:`pump`
- :doc:`check-valve`
- :doc:`vfd`
- :doc:`pump-with-vfd`
- :doc:`pump-with-vfd`

Graphviz
--------

.. graphviz::

        digraph G {
    node [fontname="DejaVu Sans"];
    node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node2 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
    node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
    node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
    node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> >];
    node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>mapsto</B></td></tr><tr><td href='urn:___param___#mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#mapsto</font></td></tr></table> >];
    node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>medium</B></td></tr><tr><td href='urn:___param___#medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#medium</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:mapsTo</font> >];
        node2 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node2 -> node3 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasMedium</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>InletConnectionPoint</B></td></tr><tr><td href='http://data.ashrae.org/standard223#InletConnectionPoint' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#InletConnectionPoint</font></td></tr></table> >];
        node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>mapsto</B></td></tr><tr><td href='urn:___param___#mapsto' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#mapsto</font></td></tr></table> >];
        node3 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>medium</B></td></tr><tr><td href='urn:___param___#medium' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#medium</font></td></tr></table> >];
        }
        
