# -*- coding: utf-8 -*-
"""sql lexer."""

from . import tokens
from .compat import bytes_type, text_type, file_type
from .keywords import SQL_REGEX
from .utils import consume


class Lexer():
    """Lexer."""

    @staticmethod
    def get_tokens(text):
        """Return an iterable of (tokentype, value) pairs generated from
        `text`."""
        iterable = enumerate(text)
        for pos, char in iterable:
            for rexmatch, action in SQL_REGEX:
                _m = rexmatch(text, pos)

                if not _m:
                    continue
                elif isinstance(action, tokens._TokenType):
                    yield action, _m.group()
                elif callable(action):
                    yield action(_m.group())

                consume(iterable, _m.end() - pos - 1)
                break
            else:
                yield tokens.Error, char


def tokenize(sql):
    """Tokenize sql."""
    return Lexer().get_tokens(sql)
