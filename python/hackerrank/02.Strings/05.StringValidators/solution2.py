#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.23

https://github.com/jerodg/hackerrank
"""

import sys
import traceback

if __name__ == '__main__':
    try:
        s = input()
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isdigit() for c in s))
        print(any(c.islower() for c in s))
        print(any(c.isupper() for c in s))
        print('\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
