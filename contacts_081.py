#!/usr/bin/env python3

class Contact(object):
   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return f"{self.name} {self.phone} {self.email}"

class ContactList(object):
   def __init__(self, d=None):
      if d is None:
         self.d = {}
      else:
         self.name = d.name
         self.phone = d.phone
         self.email = d.email
         self.d = {d.name: f"{d.name} {d.phone} {d.email}"}

   def add_contact(self, other):
      self.d[other.name] = f"{other.name} {other.phone} {other.email}"
      return self

   def get_contact(self, other):
      try:
         return self.d[other]
      except KeyError:
         return None

   def del_contact(self, other):
      try:
         del(self.d[other])
      except KeyError:
         return None

   def __str__(self):
      ls = [self.d[k] for k in sorted(list(self.d.keys()))]
      st = "\n".join(ls)
      return f"Contact list\n------------\n{st}"
