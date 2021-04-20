#!/usr/bin/env python3

import sys
#len of p2 = high
#len of p1 = long
#len of same alphy index same + 1

def findindex(p1, p2):
   l = [p1, p2]
   l = sorted(l, key=len)
   i = 0
   while i < len(l[0]) and l[0][i] != l[1][i]:
      i += 1
   index = i
   return index

def main():
   for line in sys.stdin:
      p1, p2 = line.strip().split()
      n = findindex(p1, p2)
   high = len(p2)
   length = len(p1)
   for i in range(n):
      print("." * n + p2[i] + "." * (length - n - 1))
   print(p1)
   for i in range(n + 1, high):
      print("." * n + p2[i] + "." * (length - n - 1))


if __name__ == "__main__":
   main()
