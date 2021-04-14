#!/usr/bin/env python3

class Student(object):
   def __init__(self, name, address, sid):
      self.name = name
      self.address = address
      self.sid = sid

   def __str__(self):
      return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"

class Classlist(object):
   def __init__(self):
      self.dic = {}

   def add(self, other):
      self.dic[other.sid] = other

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
