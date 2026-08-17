"""
Problem: 1352A - Sum of Round Numbers
Rating: 800
Link: https://codeforces.com/problemset/problem/1352/A

Idea:
Process the number digit by digit. For every non-zero digit, construct its
corresponding round number by multiplying the digit by the appropriate power
of 10. Ignore zero digits since they contribute nothing. The resulting
non-zero round numbers form the minimum number of summands.
"""

t=int(input())
for _ in range(t):
    n=int(input())
    ans=[]
    pow=0
    while n:
        d=n%10
        a=d*(10**pow)
        if a:
            ans.append(a)
        n=n//10
        pow+=1
    print(len(ans))
    for i in ans:
        print(i,end=" ")
    print()
