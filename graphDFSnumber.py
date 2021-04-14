#!/usr/bin/env python3

class Graph(object):
  def __init__(self, num):
    self.num = num
    self.adj = {}
    for c in range(num):
      self.adj[c] = list()
  def addEdge(self, start, end):
    self.adj[start].append(end)
    self.adj[end].append(start)

class DFSPaths(object):
  def __init__(self, gra, start):
    self.gra = gra
    self.start = start
    self.visited = [False for _ in range(gra.num)]
    self.parent = [False for _ in range(gra.num)]
    self.dfs(start)

  def dfs(self, visit):
    self.visited[visit] = True
    for w in self.gra.adj[visit]:
      if not self.visited[w]:
        self.parent[w] = visit
        self.dfs(w)

  def hasPathTo(self, end):
    return self.visited[end]

  def pathTo(self, end):
    if not self.hasPathTo(end):
      return None
    path = [end]
    while end != self.start:
      end = self.parent[end]
      path.append(end)
    return path[::-1]


