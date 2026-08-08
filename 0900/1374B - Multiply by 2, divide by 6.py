"""
Problem: 1374B - Multiply by 2, divide by 6
Rating: 900
Link: https://codeforces.com/problemset/problem/1374/B

Idea:
Factorize n into powers of 2 and 3. If n contains any other prime factor,
it is impossible to obtain 1. Also, the number of factors of 2 cannot be
greater than the number of factors of 3, because every division by 6 removes
one factor of each. If there are fewer 2s, multiply by 2 enough times to make
their counts equal, then divide by 6 repeatedly until reaching 1.
"""

t=int(input())
for _ in range(t):
    n=int(input())
    two=three=0
    while n%2==0:
        two+=1
        n=n//2
    while n%3==0:
        three+=1
        n=n//3
    if n!=1 or two>three:
        print(-1)
    else:
        print(2*three-two)
