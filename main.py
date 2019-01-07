# -*- coding: utf-8 -*-
"""bootstrap."""

import pysqlparser


def main():
    """bootstrap function."""
    _stmts = pysqlparser.split('select 1;select 1;')
    print(_stmts)


if __name__ == '__main__':
    main()
