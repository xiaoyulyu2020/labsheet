#!/usr/bin/env python3

class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.time_dict = {}
   def __str__(self):

      s = []
      s.append(f"Name :{self.name}")
      s.append(f"ID: {self.tid}")
      s.append(f"Race time: {self.get_total()}")
      return "\n".join(s)

   def add_time(self, sport, time):
      self.time_dict[sport] = time

   def get_time(self, sport):
      return self.time_dict[sport]

   def get_total(self):
      m = sum(self.time_dict.values())
      return m

def sortby(cl):
   return cl.name

def sortbysumtime(cl):
   return cl.get_total()

class Triathlon(object):
   def __init__(self):
      self.tid_cla_dict = {}

   def add(self, other):
      self.tid_cla_dict[other.tid] = other

   def lookup(self, tid):
      if tid in self.tid_cla_dict:
         return self.tid_cla_dict[tid]
      return None

   def remove(self, tid):
      if tid in self.tid_cla_dict:
         del (self.tid_cla_dict[tid])

   def __str__(self):
      sort_list = sorted(self.tid_cla_dict.values(), key=sortby)
      slist = [f"{c}" for c in sort_list]
      return "\n".join(slist)

   def best(self):
      return min(self.tid_cla_dict.values(), key=sortbysumtime)

   def worst(self):
      return max(self.tid_cla_dict.values(), key=sortbysumtime)