#!/usr/bin/env python3

import sys

def paper_rock_scissors(p1, p2):
   if p1 == p2:
      return "Draw"
   elif p1 == "rock" and p2 == "scissors":
      return "Player 1 wins"
   elif p1 == "paper" and p2 == "rock":
      return "Player 1 wins"
   elif p1 == "scissors" and p2 == "paper":
      return "Player 1 wins"
   else:
      return "Player 2 wins"

def main():
   for line in sys.stdin:
      lines = line.strip().split()
      p1, p2 = lines[0], lines[1]
      print(paper_rock_scissors(p1, p2))

if __name__ == "__main__":
   main()
