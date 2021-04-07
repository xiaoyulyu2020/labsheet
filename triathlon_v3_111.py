#!/usr/bin/env python3

class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.dic = {}

   def add_time(self, sport, time):
      if sport not in self.dic:
         self.dic[sport] = time
         return

   def get_time(self, sport):
      return self.dic[sport]

   def get_total(self, dic):
      return sum(self.dic.values())

   def __eq__(self, other):
      return self.get_total(self.dic) == other.get_total(other.dic)

   def __gt__(self, other):
      return self.get_total(self.dic) > other.get_total(other.dic)

   def __lt__(self, other):
      return self.get_total(self.dic) < other.get_total(other.dic)

   def __str__(self):
      return f"Name: {self.name}\nID: {self.tid}\nRace time: {self.get_total(self.dic)}"

class Triathlon(object):
   def __init__(self):
      self.dic = {}
      self.id = {}

   def add(self, other):
      self.dic[other.name] = other.get_total(other.dic)
      self.id[other.name] = other.tid
      return

   def best(self):
      besttime = min(self.dic.values())
      for c in self.dic:
         if self.dic[c] == besttime:
            return f"Name: {c}\nID: {self.id[c]}\nRace time: {besttime}"

   def worst(self):
      worsttime = max(self.dic.values())
      for c in self.dic:
         if self.dic[c] == worsttime:
            return f"Name: {c}\nID: {self.id[c]}\nRace time: {worsttime}"
