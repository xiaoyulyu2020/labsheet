#!/usr/bin/env python3

class Student(object):
   def __init__(self, name, address, sid):
      self.name = name
      self.address = address
      self.sid = sid
      self.dic = {}

   def __str__(self):
      return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\nAverage mark: {self.get_ave():.2f}"

   def add_mark(self, subject, mark):
      self.dic[subject] = mark

   def get_mark(self, subject):
      try:
         return self.dic[subject]
      except KeyError:
         return f"Not registered for module"

   def get_ave(self):
      if len(self.dic):
         return sum(self.dic.values()) / len(self.dic)
      return 0
