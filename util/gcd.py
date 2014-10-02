#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
