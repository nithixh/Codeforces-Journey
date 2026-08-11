"""
Problem: 1829A - Love Story
Rating: 800
Link: https://codeforces.com/problemset/problem/1829/A

Idea:
Compare every character with the actual string "codeforces"
Increment the count for each differing character
print the count
"""

t=int(input())
for _ in range(t):
    s=input()
    st="codeforces"
    ans=0
    for i in range(10):
        if s[i]!=st[i]:
            ans+=1
    print(ans)
