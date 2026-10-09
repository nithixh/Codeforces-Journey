"""
Problem: 1256A - Payment Without Change
Rating: 1000
Link: https://codeforces.com/problemset/problem/1256/A

Idea:
First, check whether the required amount S exceeds the total value
of all available coins. If it does, print NO.

Otherwise, calculate the maximum number of coins of value n that
can be used without exceeding S.

Use as many such coins as possible, but not more than the available
number a. Calculate the remaining amount after using these coins.

If the remaining amount is less than or equal to b, we have enough
coins of value 1 to pay the exact amount, so print YES.
Otherwise, print NO.
"""

q=int(input())
while q!=0:
    a,b,n,s=map(int,input().split())
    tot=a*n+b
    if s>tot:
        print("NO")
    else:
        amt=0
        ncoins=s//n
        if a>ncoins:
            amt=ncoins*n
        else:
            amt=a*n
        if (s-amt)<=b:
            print("YES")
        else:
            print("NO")
    q-=1
