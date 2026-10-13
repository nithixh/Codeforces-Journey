"""
Problem: 1326A - Bad Ugly Numbers
Rating: 1000
Link: https://codeforces.com/problemset/problem/1326/A

Idea:
If n = 1, print -1 because every one-digit number is divisible by itself.

Otherwise, construct a number with n digits by printing n - 1
nines followed by an 8.

The number ends in 8, so it is not divisible by 2.
Its digit sum is 9 * (n - 1) + 8 = 9n - 1, which is not
divisible by 9. Therefore, it is not divisible by 3 or 9.

All digits are non-zero, and the number is not divisible by any
of its digits, so this construction is valid.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print("9" * (n - 1) + "8")
