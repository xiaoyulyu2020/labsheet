#!/usr/bin/env python3

class Score(object):
   def __init__(self, goal=0, point=0):
      self.goal = goal
      self.point = point

   def score2points(self):
      return self.goal * 3 + self.point

   def __str__(self):
      return f"{self.goal} goal(s) and {self.point} point(s)"

   def __mul__(self, other):
      return Score(self.goal * 2, self.point * 2)

   def __gt__(self, other):
      return self.score2points() > other.score2points()

   def __rmul__(self, other):
      return Score(self.goal * 2, self.point * 2)

   def __imul__(self, other):
      self.goal *= 2
      self.point *= 2
      return Score(self.goal, self.point)

   def __eq__(self, other):
      return self.score2points() == other.score2points()

   def __lt__(self, other):
      return self.score2points() < other.score2points()

   def __le__(self, other):
      return self.score2points() <= other.score2points()

   def __ge__(self, other):
      return self.score2points() >= other.score2points()

   def __ne__(self, other):
      return not self.score2points() == other.score2points()

   def __add__(self, other):
      return Score(self.goal + other.goal, self.point + other.point)

   def __sub__(self, other):
      return Score(self.goal - other.goal, self.point - other.point)

   def __iadd__(self, other):
      self.goal += other.goal
      self.point += other.point
      return self

   def __isub__(self, other):
      self.goal -= other.goal
      self.point -= other.point
      return self
