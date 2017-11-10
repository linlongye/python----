# -*- coding:utf-8 -*-
"""希尔排序"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
