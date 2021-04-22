#!/usr/bin/env python3

def partition(arr, p, r):
    q = j = p
    while j < r:
        if arr[j] <= arr[r]:
            arr[q], arr[j] = arr[j], arr[q]
            q += 1
        j+= 1
    arr[q], arr[r] = arr[r], arr[q]
    return q


def qs(arr, p, r):
    if p >= r:
        return
    q = partition(arr, p , r)
    qs(arr, p, q - 1)
    qs(arr, q + 1, r)
