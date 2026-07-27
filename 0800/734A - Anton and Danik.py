"""
Problem: 734A - Anton and Danik
Rating: 800
Link: https://codeforces.com/problemset/problem/734/A

Idea:
Maintain a single counter to track the difference between Anton's and Danik's
wins. Increment it whenever Anton wins and decrement it whenever Danik wins.
If the final counter is positive Anton wins, if negative Danik wins, and if
it is zero they have won the same number of games.
"""

n=int(input())
s=input()
c=0
for i in s:
    if i=='A':
        c+=1
    else:
        c-=1
if c>0:
    print("Anton")
elif c<0:
    print("Danik")
else:
    print("Friendship")
