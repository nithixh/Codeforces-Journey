"""
Problem: 124A - The number of positions
Rating: 1000
Link: https://codeforces.com/problemset/problem/124/A

Idea:
Check every possible position Petr can occupy.

For a position i, there are i - 1 people in front of him and n - i
people behind him.

The position is valid if there are at least a people in front and
at most b people behind.

Count all positions satisfying both conditions.
"""

n,a,b=map(int,input().split())
ans=0
for i in range(a+1,n+1):
    front=i-1
    back=n-i
    if front>=a and back<=b:
        ans+=1
print(ans)
