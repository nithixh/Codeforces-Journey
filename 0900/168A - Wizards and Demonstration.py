"""
Problem: 168A - Wizards and Demonstration
Rating: 900
Link: https://codeforces.com/problemset/problem/168/A

Idea:
The required number of people is at least y% of n.

Calculate the minimum required people using ceiling division:
    required = (n * y + 99) // 100

The x wizards will definitely attend.
If x is already enough, no clones are needed.
Otherwise, create exactly required - x clones.
"""

n, x, y = map(int, input().split())
required = (n * y + 99) // 100
print(max(0, required - x))
