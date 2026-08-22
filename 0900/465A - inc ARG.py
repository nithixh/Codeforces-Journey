"""
Problem: 465A - inc ARG
Rating: 900
Link: https://codeforces.com/problemset/problem/465/A

Idea:
Since the first bit is the least significant bit, adding 1 starts from the
beginning of the string. All consecutive 1s become 0s, and the first 0
becomes 1. Therefore, count the consecutive 1s from the beginning and add 1.
If all bits are 1, every bit changes, so the answer is n.
"""

n=int(input())
s=input()
ans=0
for i in range(n):
    if s[i]=='1':
        ans+=1
    else:
        break
if ans<n:
    ans+=1

print(ans)
