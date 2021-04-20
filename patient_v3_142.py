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
