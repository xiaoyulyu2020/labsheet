class Student:
   def __init__(self, surname, forename, sid, modlist=None):
      self.sid = sid
      self.surname = surname
      self.forename = forename
      if modlist is None:
         self.modlist = []
      else:
         self.modlist = modlist

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.modlist.remove(module)

   def print_details(self):
      print(f"ID: {self.sid}")
      print(f"Surname: {self.surname}")
      print(f"Forename: {self.forename}")
      modlist = " ".join(self.modlist)
      print(f"Modules: {modlist}")