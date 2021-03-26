#!/usr/bin/env python3

import sys

def main():
   speed = 1

   class Light(object):
      def __init__(self, D, R, G):
         self.D = int(D)
         self.R = int(R)
         self.G = int(G)

      def is_red(self, time_bef_arri):
         return (time_bef_arri % (self.R + self.G)) < self.R

      def time_waite(self, time_bef_arri):
         if self.is_red(time_bef_arri):
            return self.R - (time_bef_arri % (self.R + self.G))
         else:
            return 0

   lines = [line.rstrip() for line in sys.stdin]
   roadlen = int(lines[0])
   light_list = [light.split() for light in lines[1:]]
   classlightlist = []
   for light in light_list:
      D, R, G = light
      classlight = Light(D, R, G)
      classlightlist.append(classlight)
   n = len(classlightlist)

   def totalwaite(n):
      if n == 0:
         time_bef_arri = 0
         return 0
      light = classlightlist[n - 1]
      time_bef_arri = light.D // speed + totalwaite(n - 1)
      return totalwaite(n - 1) + classlightlist[n - 1].time_waite(time_bef_arri)
   print(totalwaite(n) + roadlen // speed)

if __name__ == "__main__":
   main()
