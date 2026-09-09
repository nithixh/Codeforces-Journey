"""
Problem: 870A - Search for Pretty Integers
Rating: 900
Link: https://codeforces.com/problemset/problem/870/A

Idea:
First check if the two lists have a common digit. If they do, the smallest
common digit itself is the answer.

Otherwise, the answer must be a two-digit number. Take the smallest digit
from each list and put the smaller one first.
"""

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
amin=min(a)
bmin=min(b)
common=set(a)&set(b)
if common:
    print(min(common))
elif amin<bmin:
    print(str(amin)+str(bmin))
else:
    print(str(bmin)+str(amin))
