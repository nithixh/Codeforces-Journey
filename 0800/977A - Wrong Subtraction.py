"""
Problem: 977A - Wrong Subtraction
Rating: 800
Link: https://codeforces.com/problemset/problem/977/A

Idea:
Perform the given operation exactly k times. If the last digit of the number is
0, remove it by dividing the number by 10; otherwise, subtract 1. Print the
result after all operations.
"""

n,k=map(int,input().split())
for _ in range(k):
    if n%10==0:
        n=n//10
    else:
        n-=1
print(n)
