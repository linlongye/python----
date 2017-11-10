# -*- coding:utf-8 -*-
"""希尔排序"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2
    return alist


if __name__ == "__main__":
    print(shell_sort([34, 32, 12, 56, 23, 98]))
