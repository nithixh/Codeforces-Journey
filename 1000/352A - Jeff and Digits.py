"""
Problem: 352A - Jeff and Digits
Rating: 1000
Link: https://codeforces.com/problemset/problem/352/A

Idea:
A number is divisible by 90 if it is divisible by both 9 and 10.

Since the only digits are 5 and 0:
- We need at least one 0 for divisibility by 10.
- The sum of digits must be divisible by 9.
  Since every 5 contributes 5, the number of 5s must be a multiple of 9.

To make the largest possible number, use as many 5s as possible,
but only a multiple of 9, followed by all the available zeros.

If there are no zeros, it is impossible.
If there are fewer than 9 fives, the only possible answer is 0.
"""

n = int(input())
a = list(map(int, input().split()))
fives = a.count(5)
zeros = a.count(0)
if zeros == 0:
    print(-1)
elif fives < 9:
    print(0)
else:
    fives = (fives // 9) * 9
    print("5" * fives + "0" * zeros)
