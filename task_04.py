#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

LONGSTR = 'long' if len(MYINPUT) > MAX_LENGTH else LONGSTR

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
