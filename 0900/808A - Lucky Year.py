"""
Problem: 808A - Lucky Year
Rating: 900
Link: https://codeforces.com/problemset/problem/808/A

Idea:
A lucky year has at most one non-zero digit.

Find the place value of the first digit (1, 10, 100, 1000, etc.).

The next lucky year is the next multiple of this place value.
If the current year is already a multiple, we must go to the
following multiple.

Subtract the current year from the next lucky year to get the answer.
"""

n = int(input())
p = 1
while p <= n:
    p *= 10
p //= 10
next_year = ((n // p) + 1) * p
print(next_year - n)
