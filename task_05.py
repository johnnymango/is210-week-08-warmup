#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The BP Test."""

BP_STATUS = int(raw_input('What is your blood pressure? '))

if BP_STATUS <= 89:
    BP_STATUS = 'Low'
elif 90 <= BP_STATUS <= 119:
    BP_STATUS = 'Ideal'
elif 120 <= BP_STATUS <= 139:
    BP_STATUS = 'Warning'
elif 140 <= BP_STATUS <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

RESULTS = 'Your status is currently: {}!'.format(BP_STATUS)
print RESULTS