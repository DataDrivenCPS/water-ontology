
on-off-command
##############

.. tabs::

    .. tab:: Turtle

        .. code:: turtle

           @prefix P: <urn:___param___#> .
           @prefix ns1: <http://data.ashrae.org/standard223#> .
           
           P:name a ns1:EnumeratedActuatableProperty ;
               ns1:hasEnumerationKind ns1:EnumerationKind-OnOff .
           
           

    .. tab:: With Inline Dependencies

        .. code:: turtle

            @prefix P: <urn:___param___#> .
            @prefix ns1: <http://data.ashrae.org/standard223#> .

            P:name a ns1:EnumeratedActuatableProperty ;
                ns1:hasEnumerationKind ns1:EnumerationKind-OnOff .



Parameters
----------

- name


Dependencies
------------



Dependents
----------

- :doc:`pump-with-vfd`

Graph Visualization
--------------------

.. tabs::

    .. tab:: Template

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasEnumerationKind</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumeratedActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumeratedActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumeratedActuatableProperty</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumerationKind-OnOff</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumerationKind-OnOff' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumerationKind-OnOff</font></td></tr></table> >];
            }
            

    .. tab:: With Inline Dependencies

        .. graphviz::

                digraph G {
            node [fontname="DejaVu Sans"];
            node0 -> node1 [color=BLACK, label=< <font point-size='10' color='#336633'>ns1:hasEnumerationKind</font> >];
            node0 -> node2 [color=BLACK, label=< <font point-size='10' color='#336633'>rdf:type</font> >];
            node0 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>name</B></td></tr><tr><td href='urn:___param___#name' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>urn:___param___#name</font></td></tr></table> >];
            node1 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumerationKind-OnOff</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumerationKind-OnOff' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumerationKind-OnOff</font></td></tr></table> >];
            node2 [shape=none, color=black, label=< <table color='#666666' cellborder='0' cellspacing='0' border='1'><tr><td colspan='2' bgcolor='grey'><B>EnumeratedActuatableProperty</B></td></tr><tr><td href='http://data.ashrae.org/standard223#EnumeratedActuatableProperty' bgcolor='#eeeeee' colspan='2'><font point-size='10' color='#6666ff'>http://data.ashrae.org/standard223#EnumeratedActuatableProperty</font></td></tr></table> >];
            }
            
