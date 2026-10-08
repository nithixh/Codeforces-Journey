"""
Problem: 102B - Sum of Digits
Rating: 1000
Link: https://codeforces.com/problemset/problem/102/B

Idea:
Keep replacing the number with the sum of its digits until it becomes
a single-digit number.

Since n can contain up to 100000 digits, read it as a string.

For every step, calculate the sum of all digits and convert the sum
back to a string. Count how many times this operation is performed.

If the original number is already a single digit, the answer is 0.
"""

n = input()
ans = 0
while len(n) > 1:
    total = 0
    for digit in n:
        total += int(digit)
    n = str(total)
    ans += 1
print(ans)
