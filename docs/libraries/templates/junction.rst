
junction
########

.. tabs::

    .. tab:: Turtle

        .. code:: turtle

           @prefix P: <urn:___param___#> .
           @prefix ns1: <http://data.ashrae.org/standard223#> .
           
           P:name a ns1:Junction .
           
           

    .. tab:: With Inline Dependencies

        .. code:: turtle

            @prefix P: <urn:___param___#> .

            P:name a <http://data.ashrae.org/standard223#Junction> .



Parameters
----------

- name


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
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Junction</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Junction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Junction</font></td></tr></table> >];
            }
            

    .. tab:: With Inline Dependencies

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>Junction</B></td></tr><tr><td href='http://data.ashrae.org/standard223#Junction' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#Junction</font></td></tr></table> >];
            }
            
