"""
Problem: 742A - Arpa's hard exam and Mehrdad's naive cheat
Rating: 900
Link: https://codeforces.com/problemset/problem/742/A

Idea:
We need to find the last digit of 1378^n.

The last digit depends only on the last digit of the base (8).

The powers of 8 have a repeating cycle of 4:
    8, 4, 2, 6

Therefore, use n % 4 to find the position in the cycle.

Special case:
If n == 0, the answer is 1 because any non-zero number
raised to the power 0 is 1.
"""

n = int(input())
cycle = [6, 8, 4, 2]
if n == 0:
    print(1)
else:
    print(cycle[n % 4])
