"""
Problem: 1237A - Balanced Rating Changes
Rating: 1000
Link: https://codeforces.com/problemset/problem/1237/A

Idea:
Divide every rating change by 2, keeping the result as close as possible
to the exact value.

If a number is even, simply divide it by 2.

If a number is odd, its result can be either the floor or ceiling
of half the number. Alternate between rounding up and rounding down
for odd numbers to keep the total sum equal to 0.

Python's // operator automatically rounds down, including for
negative numbers.
"""

n = int(input())
round_up = True
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        print(a // 2)
    else:
        if round_up:
            print((a + 1) // 2)
        else:
            print((a - 1) // 2)
        round_up = not round_up
