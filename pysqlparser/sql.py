# -*- coding: utf-8 -*-
"""This module contains classes representing syntactical elements of SQL."""

import re

from . import tokens as T
from .compat import text_type, string_types


class Token():
    """Base class for all other classes in this module."""

    __slots__ = ('value', 'ttype', 'parent', 'normalized', 'is_keyword',
                 'is_group', 'is_whitespace')

    def __init__(self, ttype, value):
        value = text_type(value)
        self.value = value
        self.ttype = ttype
        self.parent = None
        self.is_group = False
        self.is_keyword = ttype in T.Keyword
        self.is_whitespace = self.ttype in T.Whitespace
        self.normalized = value.upper() if self.is_keyword else value

    def __str__(self):
        return self.value

    def __repr__(self):
        # pylint: disable=possibly-unused-variable,invalid-name
        cls = self._get_repr_name()
        value = self._get_repr_value()

        q = '"' if value.startswith("'") and value.endswith("'") else "'"
        return '<{cls} {q}{value}{q} at 0x{id:2X}>'.format(
            id=id(self), **locals())

    def _get_repr_name(self):
        return str(self.ttype).split('.')[-1]

    def _get_repr_value(self):
        raw = text_type(self)
        if len(raw) > 7:
            raw = raw[:6] + '...'
        return re.sub(r'\s+', ' ', raw)

    def flatten(self):
        """Resolve subgroups."""
        yield self

    def match(self, ttype, values, regex=False):
        """Checks whether the token matches the given arguments."""
        type_matched = self.ttype is ttype
        if not type_matched or values is None:
            return type_matched

        if isinstance(values, string_types):
            values = (values,)

        if regex:
            # TODO: Add test for regex with is_keyborad = false
            flag = re.IGNORECASE if self.is_keyword else 0
            values = (re.compile(v, flag) for v in values)

            for pattern in values:
                if pattern.search(self.normalized):
                    return True
            return False

        if self.is_keyword:
            values = (v.upper() for v in values)

        return self.normalized in values

    def within(self, group_cls):
        """Returns ``True`` if this token is within *group_cls*."""
        parent = self.parent
        while parent:
            if isinstance(parent, group_cls):
                return True
            parent = parent.parent
        return False

    def is_child_of(self, other):
        """Returns ``True`` if this token is a direct child of *other*."""
        return self.parent == other

    def has_ancestor(self, other):
        """Returns ``True`` if *other* is in this tokens ancestry."""
        parent = self.parent
        while parent:
            if parent == other:
                return True
            parent = parent.parent
        return False
