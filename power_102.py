#!/usr/bin/env python3

def power(n, m):
   if n == 0 and m != 0:
      return 0
   if n == 1:
      return 1
   if m == 0:
      return 1
   if m == 1:
      return n
   return n * power(n, m - 1)
