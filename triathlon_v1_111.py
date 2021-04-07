#!/usr/bin/env python3


class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def __str__(self):
      return f"Name: {self.name}\nID: {self.tid}"

class Triathlon(object):
   def __init__(self):
      self.dic = {}

   def add(self, other):
      self.dic[other.name] = other.tid
      return

   def lookup(self, value):
      for c in self.dic:
         if self.dic[c] == value:
            return Triathlete(c, value)
         return None

   def remove(self, value):
      for c in self.dic:
         if self.dic[c] == value:
            del self.dic[c]
            return self.dic
