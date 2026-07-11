"""
Problem : 282A - Bit++
Rating : 800
Link : https://codeforces.com/problemset/problem/282/A

Idea:
initialize x with 0
If the operation contains a +, increment the value of x
else, decrement the value of x
"""

n=int(input())
x=0
for _ in range(n):
    op=input()
    if '+' in op:
        x+=1
    else:
        x-=1
print(x)
