#!/usr/bin/env python3

import sys

def checksame(s):
   stack = []
   i = 0
   while i < len(s):
      if s[i] in s[i + 1:] or s[i] in stack:
         stack.append(s[i])
      i += 1
   n = len(s) - len(stack)
   if stack == []:
      n = len(s) - 2
   return n

def main():
   for line in sys.stdin:
      s = list(line.rstrip())
      print(checksame(s))

if __name__ == "__main__":
   main()
