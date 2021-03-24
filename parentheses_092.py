#!/usr/bin/env python3

def matcher(line):
   d = {")": "(", "}": "{", "]": "["}

   class Stack(object):
      def __init__(self):
         self.s = []

      def push(self, key):
         return self.s.append(key)

      def pop(self):
         return self.s.pop()

      def is_empty(self):
         return len(self.s) == 0

   s = Stack()
   for k in line:
      if k in d.values():
         s.push(c)
      if k in d.keys():
         try:
            if d[k] != s.pop():
               return False
         except IndexError:
            return False
   return s.is_empty()
