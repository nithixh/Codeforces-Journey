"""
Problem: 408A - Line to Cashier
Rating: 900
Link: https://codeforces.com/problemset/problem/408/A

Idea:
For each cashier, calculate the total time needed for all
people already standing in that queue.

Each person takes:
    (number of items * 5) + 15 seconds

The 15 seconds is added once per customer for payment.
Find the minimum total time among all cashiers.
"""

n = int(input())
k = list(map(int, input().split()))
ans = float('inf')
for i in range(n):
    items = list(map(int, input().split()))
    total_time = sum(items) * 5 + k[i] * 15
    ans = min(ans, total_time)
print(ans)
