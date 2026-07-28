"""
Problem: 1742A - Sum
Rating: 800
Link: https://codeforces.com/problemset/problem/1742/A

Idea:
For each test case, check all three possible combinations to see whether one
number is equal to the sum of the other two. If any condition is satisfied,
print "YES"; otherwise, print "NO".
"""

t=int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if (a+b==c) or (a+c==b) or (c+b==a):
        print("YES")
    else:
        print("NO")
