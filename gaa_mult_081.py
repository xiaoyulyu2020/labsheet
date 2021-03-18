#!/usr/bin/env python3

class Score(object):
   def __init__(self, goal=0, point=0):
      self.goal = goal
      self.point = point

   def __str__(self):
      return f"{self.goal} goal(s) and {self.point} point(s)"

   def __mul__(self, other):
      return Score(self.goal * 2, self.point * 2)

   def __gt__(self, other):
      return self.point > other.point

   def __rmul__(self, other):
      return Score(self.goal * 2, self.point * 2)

   def __imul__(self, other):
      self.goal *= 2
      self.point *= 2
      return Score(self.goal, self.point)

   def __eq__(self, other):
      return self.point == other.point
