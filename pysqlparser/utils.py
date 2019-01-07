# -*- coding: utf-8 -*-
"""utilities."""

import itertools

from collections import deque


def consume(iterator, steps):
    """Advance the iterator n-steps ahead. If n is none, consume entirely."""
    deque(itertools.islice(iterator, steps), maxlen=0)
