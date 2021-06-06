#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = list(map(int, input().split()))
    print('максимальный элемент имеет номер ', A.index(max(A)))
    zero_1 = zero_2 = -1
    for i, item in enumerate(A):
        if (item == 0) and (zero_1 != -1) and (zero_2 == -1):
            zero_2 = i
        if (item == 0) and (zero_1 == -1):
            zero_1 = i
    print('первый нулевой элемент в позиции ', zero_1, ' второй нулевой элемент в позиции ', zero_2)
    mult = 1
    for item in A[zero_1 + 1:zero_2]:
        mult *= item
    print('произведение элементов между нулевыми элементами ', mult)
    B = []
    C = []
    for i, item in enumerate(A):
        if i % 2 == 0:
            B.append(A[i])
        else:
            C.append(A[i])
    A = C + B
    print(A)
