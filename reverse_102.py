#!/usr/bin/env python3

def reverse_list(n):
   if len(n) <= 1:
      return n
   return reverse_list(n[1:]) + [n[0]]
