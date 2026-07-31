"""
Problem: 1030A - In Search of an Easy Problem
Rating: 800
Link: https://codeforces.com/problemset/problem/1030/A

Idea:
If at least one person considers the problem hard (response = 1), the answer
is "HARD". Otherwise, if all responses are 0, the answer is "EASY".
"""

n=int(input())
response = list(map(int,input().split()))
if response.count(1):
    print("HARD")
else:
    print("EASY")
