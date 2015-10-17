#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

MYTEST = LOOKS_NICE and EXPENSE <= MAX_EXPENSE
SACRIFICE = True if not MYTEST else GET_OUT_ALIVE