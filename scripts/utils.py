#!/usr/bin/env python

def is_number(s):
    try:
        n = float(s)
        return n
    except ValueError:
        return float('nan')