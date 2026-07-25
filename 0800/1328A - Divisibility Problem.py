"""
Problem: 1328A - Divisibility Problem
Rating: 800
Link: https://codeforces.com/problemset/problem/1328/A

Idea:
If a is already divisible by b, no moves are needed. Otherwise, find the next
multiple of b greater than a. The difference between this multiple and a gives
the minimum number of increments required to make a divisible by b.
"""

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if not (a%b):
        print(0)
    else:
        div=a//b
        print((b*(div+1))-a)
