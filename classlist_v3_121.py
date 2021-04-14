#!/usr/bin/env python3

class Student(object):
   def __init__(self, name, address, sid):
      self.name = name
      self.address = address
      self.sid = sid
      self.dic = {}

   def __str__(self):
      return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"

   def add_mark(self, subject, mark):
      self.dic[subject] = mark

   def get_mark(self, subject):
      try:
         return self.dic[subject]
      except KeyError:
         return f"Not registered for module"

class Classlist(object):
   def __init__(self):
      self.dic = {}

   def add(self, other):
      for c in other.dic:
         if c not in self.dic:
            self.dic[c] = 0
         else:
            self.dic[c] += 1

   def lookup(self, sid):
      for c in self.dic:
         if c == sid:
            return self.dic[c]
         return None

   def remove(self, sid):
      for c in self.dic:
         if c == sid:
            del self.dic[c]
            return self.dic

   def __str__(self):
      ls = []
      for c in sorted(self.dic.keys()):
         s = self.dic[c]
         f = f"Name: {s.name}\nAddress: {s.address}\nID: {s.sid}"
         ls.append(f)
      return "\n".join(ls)

   def least_popular_module(self):
      maxi = min(self.dic.values())
      for c in self.dic:
         if self.dic[c] == maxi:
            return c
