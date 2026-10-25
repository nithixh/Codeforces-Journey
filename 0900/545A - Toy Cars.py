"""
Problem: 545A - Toy Cars
Rating: 1000
Link: https://codeforces.com/problemset/problem/545/A

Idea:
A car is good if it never turns over in any collision.

In each row of the matrix, values 1 and 3 mean that the car
corresponding to that row turned over in a collision.

Check every row. If it contains neither 1 nor 3, that car is good.

Store the indices of all good cars and print their count,
followed by their indices in increasing order.
"""

n = int(input())
good = []
for i in range(n):
    row = list(map(int, input().split()))
    if 1 not in row and 3 not in row:
        good.append(i + 1)
print(len(good))
if good:
    print(*good)
