#!/usr/bin/env python3

def quick_sort(s):
	if len(s) <= 1:
		return s
	else:

		pivot = s.pop()
		greater = []
		smaller = []

		for num in s:
			if num > pivot:
				greater.append(num)
			else:
				smaller.append(num)
		return quick_sort(smaller) + [pivot] + quick_sort(greater)

print(quick_sort([1,3,4,23,3,4,5,3,3,65,9,7,0,3]))