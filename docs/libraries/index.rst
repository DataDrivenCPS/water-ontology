
Equipment templates rely on WaTr class defaults for their process values.
Run SHACL-AF inference with ``shifty`` before querying ``watr:hasProcess``;
for example, ``uv-reactor`` gains ``watr:Process-UVDisinfection``. An explicit
process on an instance overrides its class default.

In a BuildingMOTIF model-building context, complete defaults before compiling
the model, as shown in ``notebooks/ModelBuilder.ipynb``:

.. code-block:: python

   import shifty

   shapes = s223.get_shape_collection()
   completed = shifty.infer(ctx.compile(), shapes_graph=shapes.graph).graph()
   bldg.add_graph(completed)
   graph = bldg.compile([shapes])

This explicit step also supports BuildingMOTIF's PySHACL backend, whose
ontology import step does not copy the property-shape default annotations
into the graph queried by rules.

.. autotemplatedoc:: libraries/templates docs/libraries/

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :glob:

   templates/index.rst
