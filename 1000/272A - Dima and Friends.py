"""
Problem: 272A - Dima and Friends
Rating: 1000
Link: https://codeforces.com/problemset/problem/272/A

Idea:
If the mod of total number of people and the count of fingers is 1, then Dima has to clean the house.
Since the number of fingers he shows can only be from 1 to 5, we can find the number of ways by iterating 
through all possible answers
"""

n=int(input())
ppl=n+1
fingers=list(map(int,input().split()))
tot=sum(fingers)
ans=0
for i in range(1,6):
    if (tot+i)%ppl!=1:
        ans+=1
print(ans)
