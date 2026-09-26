"""
Problem: 1141A - Game 23
Rating: 1000
Link: https://codeforces.com/problemset/problem/1141/A

Idea:
First, m must be divisible by n because every move only multiplies n
by 2 or 3.

So we find q = m / n. For the transformation to be possible, q must
contain only factors 2 and 3.

Repeatedly divide q by 2 and 3 and count every division as one move.
If q becomes 1, all required multiplications were found, so print the
count. Otherwise, q contains another factor and the transformation is
impossible, so print -1.
"""

n,m=map(int,input().split())
if m<n:
    print(-1)
else:
    if m%n==0:
        q=m//n
        ans=0
        while q%2==0:
            q//=2
            ans+=1
        while q%3==0:
            q//=3
            ans+=1
        if q==1:
            print(ans)
        else:
            print(-1)
    else:
        print(-1)
        
