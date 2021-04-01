#!/usr/bin/env python3

def maximum(s):
   if len(s) == 1:
      return s[0]
   elif s[0] > maximum(s[1:]):
      return s[0]
   return maximum(s[1:])
