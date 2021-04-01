#!/usr/bin/env python3

def minimum(s):
   if len(s) == 1:
      return s[0]
   elif s[0] < minimum(s[1:]):
      return s[0]
   return minimum(s[1:])
