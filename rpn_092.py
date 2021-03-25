#!/usr/bin/env python3

def calculator(line):
   class Stack(object):
      def __init__(self):
         self.s = []

      def push(self, key):
         return self.s.append(key)

      def pop(self):
         return self.s.pop()

      def is_empty(self):
         return len(self.s) == 0

   def sqrt(value):
      return float(value ** 0.5)

   def negi(value):
      return float(0 - value)

   def dev(a, b):
      return float(a / b)

   def plus(a, b):
      return float(a + b)

   def mult(a, b):
      return float(a * b)

   def mi(a, b):
      return float(a - b)

   binops = {"/": dev, "+": plus, "*": mult, "-": mi}
   uniops = {"n": negi, "r": sqrt}
   s = Stack()
   for c in line.split():
      if c not in binops and c not in uniops:
         s.push(float(c))
      else:
         if c in binops:
            try:
               b = s.pop()
               a = s.pop()
               total = binops[c](a, b)
               s.push(total)
            except TypeError:
               return s
         if c in uniops:
            b = uniops[c](s.pop())
            s.push(b)
   k = s.pop()
   return float(k)
