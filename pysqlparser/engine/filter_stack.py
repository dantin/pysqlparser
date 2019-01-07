# -*- coding: utf-8 -*-
"""filter."""

from .. import lexer
from .statement_splitter import StatementSplitter


class FilterStack():
    """`FilterStack` is a stack for filter."""

    def __init__(self):
        self.preprocess = []
        self.stmtprocess = []
        self.postprocess = []
        self._grouping = True

    def run(self, sql):
        """process sql"""
        stream = lexer.tokenize(sql)
        for filter_ in self.preprocess:
            stream = filter_.process(stream)

        stream = StatementSplitter().process(stream)

        # Output: Stream processed Statements
        for stmt in stream:
            #stmt = grouping.group(stmt)

            #for filter_ in self.stmtprocess:
            #    filter_.process(stmt)

            #for filter_ in self.postprocess:
            #    stmt = filter_.process(stmt)

            yield stmt
