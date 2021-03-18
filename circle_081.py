#!/usr/bin/env python3

class Point(object):
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def midpoint(self, other):
      x = (self.x + other.x) // 2
      y = (self.y + other.y) // 2
      return Point(x, y)

   def __str__(self):
      return f"{self.x} {self.y}"

class Circle(object):
   def __init__(self, point, radius):
      self.point = point
      self.radius = radius

   def __add__(self, other):
      point = self.point.midpoint(other.point)
      radius = self.radius + other.radius
      return Circle(point, radius)

   def __str__(self):
      return f"Centre: ({self.point.x:.1f}, {self.point.y:.1f})\nRadius: {self.radius}"
