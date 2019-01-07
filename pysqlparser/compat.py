# -*- coding: utf-8 -*-
"""types"""


from io import TextIOBase, StringIO


# pylint: disable=invalid-name
bytes_type = bytes
text_type = str
string_types = (str,)
file_type = (StringIO, TextIOBase)
