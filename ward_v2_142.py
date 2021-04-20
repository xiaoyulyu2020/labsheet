#!/usr/bin/env python3

class Patient(object):

   def __init__(self, name, age, doctor, medi=None):
      self.name = name
      self.age = age
      self.doctor = doctor

      if medi:
         self.medi = medi
      else:
         self.medi = []

   def add_medication(self, medi):
      self.medi.append(medi)

   def __str__(self):
      medi = ", ".join(self.medi)
      return f"Name: {self.name}\nAge: {self.age}\nMedications: {medi}\nDoctor: {self.doctor}"

class Ward(object):

   def __init__(self):
      self.pdic = {}

   def add(self, other):
      self.pdic[other.name] = other

   def lookup(self, name):
      if name in self.pdic:
         return self.pdic[name]
      return None

   def remove(self, name):
      if name in self.pdic:
         del self.pdic[name]

   def get_patients_by_medication(self, medi):
      lis = []
      for name in self.pdic:
         if medi in self.pdic[name].medi:
            lis.append(self.pdic[name])
      return lis
