"""
Problem: 267A - Subtractions
Rating: 900
Link: https://codeforces.com/problemset/problem/267/A

Idea:
Instead of performing one subtraction at a time, we can
perform multiple subtractions in one step.

If a >= b:
    We can subtract b from a exactly a // b times.
    Add a // b to the answer and update a = a % b.

Otherwise, do the same with b.

Repeat until either number becomes zero.
This is similar to the Euclidean algorithm.
"""

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    ans = 0
    while a > 0 and b > 0:
        if a >= b:
            ans += a // b
            a %= b
        else:
            ans += b // a
            b %= a
    print(ans)
