#!/usr/bin/env python3

s = "hello"

def revers(s):
  if len(s) == 1:
    return s
  return revers(s[1:]) + s[0]

print(revers(s))