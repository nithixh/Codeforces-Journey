"""
Problem: 246A - Buggy Sorting
Rating: 900
Link: https://codeforces.com/problemset/problem/246/A

Idea:
The given sorting algorithm works correctly for n <= 2,
so no counter-example exists. Print -1 in these cases.

For n >= 3, print the numbers in descending order:
n, n-1, ..., 1.

The algorithm moves larger elements towards the right,
but because each new pass starts from the next position,
the smallest element may remain in the wrong position.

This descending array acts as a counter-example.
"""

n = int(input())
if n <= 2:
    print(-1)
else:
    print(*range(n, 0, -1))
