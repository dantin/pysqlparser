# -*- coding: utf-8 -*-
"""SQL Parser."""


from . import engine
from .compat import text_type


def split(sql):
    """Split *sql* into single statements."""
    stack = engine.FilterStack()
    return [text_type(stmt).strip() for stmt in stack.run(sql)]
