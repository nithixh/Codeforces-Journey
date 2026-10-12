"""
Problem: 610A - Pasha and Stick
Rating: 1000
Link: https://codeforces.com/problemset/problem/610/A

Idea:
The perimeter of a rectangle is n, so n must be even.
If n is odd, forming a rectangle is impossible, so print 0.

For even n, let half = n // 2.
The two different side lengths must add up to half.

Count the possible pairs of positive integer side lengths, ignoring
reversed duplicates. There are (half - 1) // 2 such pairs.

If half is even, one pair forms a square, so it must be excluded.
The formula (n - 2) // 4 gives the final answer for even n.
"""

n = int(input())
if n % 2 != 0:
    print(0)
else:
    print((n - 2) // 4)
