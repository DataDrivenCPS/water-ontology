Template Libraries
==================

The reference pages describe graph fragments generated from the current
``libraries/templates`` YAML definitions. Bind their ``P:`` parameters and
resolve dependencies with BuildingMOTIF before validating a plant model.
Equipment-class defaults and treatment-objective inference apply to instantiated
models as described in :doc:`../explanation/equipment_function`. Explicit
instance values suppress class defaults for the same property.

Complete defaults with ``shifty`` before BuildingMOTIF compilation, as shown in
``notebooks/ModelBuilder.ipynb``:

.. code-block:: python

   import shifty

   shapes = s223.get_shape_collection()
   completed = shifty.infer(ctx.compile(), shapes_graph=shapes.graph).graph()
   bldg.add_graph(completed)
   graph = bldg.compile([shapes])

This step also supports BuildingMOTIF's PySHACL backend, whose ontology import
does not copy property-shape default annotations into the graph queried by rules.

The membrane template uses generic S223 equipment with an explicit membrane
process; choose a concrete equipment or process type when the mechanism is known.
The disinfection-unit template requires a process binding because disinfection
names an objective. Its equipment class supplies the design objective.

Run ``uv run python scripts/generate_template_docs.py`` after template changes.
The navigation lists every template shipped in the library.
