"""
Problem: 2254A - Riptide
Rating: 800
Link: https://codeforces.com/problemset/problem/2254/A

Idea:
Simulate the game round by round. Before each round, check whether any two
players have the same number of tokens; if so, the game ends. Otherwise, find
the player with the most tokens and the player with the fewest tokens, transfer
one token from the former to the latter, and count the round. Repeat until two
players have equal numbers of tokens.
"""

t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    ans=0
    while a!=b and b!=c and a!=c:
        mx=max(a,b,c)
        mi=min(a,b,c)
        if a==mx:
            a-=1
            if b==mi:
                b+=1
            else:
                c+=1
        elif b==mx:
            b-=1
            if a==mi:
                a+=1
            else:
                c+=1
        else:
            c-=1
            if b==mi:
                b+=1
            else:
                a+=1
        ans+=1
    print(ans)
