#!/usr/bin/env python3

class Patient(object):

   def __init__(self, name, age, doctor, medi):
      self.name = name
      self.age = age
      self.doctor = doctor
      self.medi = medi

   def __str__(self):
      medi = ", ".join(self.medi)
      return f"Name: {self.name}\nAge: {self.age}\nMedications: {medi}\nDoctor: {self.doctor}"
