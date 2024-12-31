
controller
##########

.. code-block:: turtle

    @prefix ns2: <urn:nawi-water-ontology#> .
    @prefix ns3: <urn:___param___#> .
    
    ns3:name a ns2:Controller .
    
    

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
    node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
    node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Controller</B></td></tr><tr><td href='urn:nawi-water-ontology#Controller' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Controller</font></td></tr></table> >];
    }
    

.. collapse:: Template With Inline Dependencies

    .. graphviz::

                digraph G {
        node [fontname="DejaVu Sans"];
        node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
        node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
        node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Controller</B></td></tr><tr><td href='urn:nawi-water-ontology#Controller' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:nawi-water-ontology#Controller</font></td></tr></table> >];
        }
        
