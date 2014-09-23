#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal
from nose.tools import assert_not_equal

from util.list_helper import exclusive
from util.list_helper import intersect
from util.list_helper import union

def test_exclusive():
    assert_equal(exclusive([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2, 5, 6])

def test_intersect():
    assert_equal(intersect([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])

def test_union():
    assert_equal(union([1, 2, 3, 4], [5, 6, 7, 8]), range(1, 9))
