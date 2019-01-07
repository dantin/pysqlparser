# -*- coding: utf-8 -*-
"""statement splitter."""

from .. import tokens as T

class StatementSplitter():
    """Filter that split stream at individual statements."""

    def __init__(self):
        self._reset()

    def _reset(self):
        """Set the filter attributes to its default values."""
        self._in_declare = False
        self._is_create = False
        self._begin_depth = 0

        self.consume_ws = False
        self.tokens = []
        self.level = 0

    def process(self, stream):
        """Process the stream."""
        EOS_TTYPE = T.Whitespace, T.Comment.Single

        for ttype, value in stream:
            if self.consume_ws and ttype not in EOS_TTYPE:
                yield sql.Statement(self.tokens)
