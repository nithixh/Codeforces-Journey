"""
Problem: 412B - Network Configuration
Rating: 900
Link: https://codeforces.com/problemset/problem/412/B

Idea:
The final speed must be a speed that at least k computers can achieve.
A computer with speed greater than the chosen speed can simply be reduced
to that speed.

Therefore, we sort all speeds in descending order. The k-th largest speed
is the maximum speed that at least k computers can have.
"""

n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
print(a[k-1])
