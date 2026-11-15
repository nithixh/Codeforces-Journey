"""
Problem: 631A - Interview
Rating: 900
Link: https://codeforces.com/problemset/problem/631/A

Idea:
Bitwise OR never decreases when we add more elements.

Therefore, the maximum OR value for an array is obtained
by considering the entire array (l = 1, r = n).

Calculate the bitwise OR of all elements in array a
and all elements in array b.

Add both OR values to get the answer.
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
y = 0
for i in range(n):
    x |= a[i]
    y |= b[i]
print(x + y)
