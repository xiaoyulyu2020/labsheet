#!/usr/bin/env python3

class Queue(object):
      def __init__(self, s=None):
         if s is None:
            self.s = []
         else:
            self.s = s

      def enqueue(self, key):
         return self.s.append(key)

      def dequeue(self):
         return self.s.pop(0)

      def first(self):
         return self.s[0]

      def is_empty(self):
         return len(self.s) == 0

      def __len__(self):
         return len(self.s)
