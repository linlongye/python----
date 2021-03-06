# -*- coding:utf-8 -*-
"""插入排序"""


def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break
    return alist


if __name__ == "__main__":
    print(insert_sort([54, 26, 93, 17, 77, 31, 44, 55, 26]))
