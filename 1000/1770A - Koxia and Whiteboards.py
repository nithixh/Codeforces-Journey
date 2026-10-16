"""
Problem: 1770A - Koxia and Whiteboards
Rating: 1000
Link: https://codeforces.com/problemset/problem/1770/A

Idea:
For every operation, replace the smallest number on the whiteboards
with the given value b.

This maximizes the final sum because replacing a smaller number
instead of a larger one gives the best possible result.

Sort the initial array in ascending order, then process each b:
replace the smallest element with b and sort again.

Finally, print the sum of the array.
"""

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    for x in b:
        a[0] = x
        a.sort()
    print(sum(a))
