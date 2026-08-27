"""
Problem: 52A - 123-sequence
Rating: 900
Link: https://codeforces.com/problemset/problem/1560/A

Idea:
Count how many times each number appears in the sequence. To make all
numbers equal, we should keep the number that appears the most and replace
all other numbers. Therefore, the minimum number of replacements is n minus
the maximum frequency.
"""

n=int(input())
d={}
nums=list(map(int,input().split()))

for i in nums:
    d[i]=d.get(i,0)+1

mx=0
for i in d:
    mx=max(mx,d[i])

print(n-mx)
