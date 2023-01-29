#!/bin/python3

import math
import os
import random
import re
import sys


def reverse_game(n, k):
    if k < n//2:
        return 2*k + 1
    else:
        return 2*(n-k-1)

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        print(reverse_game(n, k))
