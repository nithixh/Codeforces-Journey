"""
Problem: 148A - Insomnia cure
Rating: 800
Link: https://codeforces.com/problemset/problem/148/A

Idea:
Each dragon is damaged if its number is divisible by at least one of k, l, m,
or n. Iterate through the multiples of each divisor up to d and store the
damaged dragon numbers in a set. Since a set keeps only unique elements, the
final size of the set gives the total number of damaged dragons.
"""

k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
damaged=set()
for i in range(k,d+1,k):
    damaged.add(i)
for i in range(l,d+1,l):
    damaged.add(i)
for i in range(m,d+1,m):
    damaged.add(i)
for i in range(n,d+1,n):
    damaged.add(i)
print(len(damaged))
