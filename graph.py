#!/usr/bin/env python3

class Graph(object):
   def __init__(self, n):
      self.adj = {}
      self.n = n
      for c in range(n):
         self.adj[c] = list()

   def add_edge(self, start, end):
      self.adj[start].append(end)
      self.adj[end].append(start)
