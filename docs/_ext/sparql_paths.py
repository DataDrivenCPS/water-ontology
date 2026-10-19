"""Highlight SPARQL's optional property paths without treating '?' as an error."""

from pygments.lexer import inherit
from pygments.lexers.rdf import SparqlLexer
from pygments.token import Operator


class SparqlPathLexer(SparqlLexer):
    tokens = {"root": [(r"\?(?=[/\s;.)}])", Operator), inherit]}


def setup(app):
    app.add_lexer("sparql", SparqlPathLexer)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
