"""
Problem: 75A - Life Without Zeros
Rating: 1000
Link: https://codeforces.com/problemset/problem/75/A

Idea:
First, calculate the sum of a and b.

Remove all zeros from the sum and store the result in nexpected.

Similarly, remove all zeros from a and b, then add the resulting
numbers to get res.

If res equals nexpected, the equation remains correct after
removing all zeros, so print YES. Otherwise, print NO.
"""

a=int(input())
b=int(input())
expected=str(a+b)
nexpected=""
for i in expected:
    if i!='0':
        nexpected+=i
nexpected=int(nexpected)
na=nb=""
a=str(a)
b=str(b)
for i in a:
    if i!='0':
        na+=i
for i in b:
    if i!='0':
        nb+=i
na=int(na)
nb=int(nb)
res=na+nb
if res==nexpected:
    print("YES")
else:
    print("NO")
