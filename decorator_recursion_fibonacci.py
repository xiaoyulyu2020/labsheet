#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize = 999999)
def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
