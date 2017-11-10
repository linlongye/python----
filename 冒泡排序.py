# -*- coding:utf-8 -*-
"""冒泡排序"""


def bubble_sort(alist):
    # for j in range(0, lens - 1):
    #     for i in range(0, lens - 1 - j):
    #         if alist[i] > alist[i + 1]:
    #             alist[i], alist[i + 1] = alist[i + 1], alist[i]
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            count = 0
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
            if count == 0:
                return
    return alist


print (bubble_sort([1]))
