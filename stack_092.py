#!/usr/bin/env python3

class Stack(object):
   def __init__(self, s=None):
      if s is None:
         self.s = []
      else:
         self.s = s

   def push(self, key):
      return self.s.append(key)

   def pop(self, key=None):
      if key is None:
         return self.s.pop()
      else:
         return self.s.pop(key)

   def top(self):
      return self.s[-1]

   def is_empty(self):
      return len(self.s) == 0

   def __len__(self):
      return len(self.s)
