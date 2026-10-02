"""
Problem: 688B - Lovely Palindromes
Rating: 1000
Link: https://codeforces.com/problemset/problem/688/B

Idea:
The first half of the n-th even-length palindrome is exactly n.

So, we can simply take n as a string and append its reverse.

For example:
n = 123
answer = 123321

Using strings is necessary because n can contain up to 100000 digits.
"""

n = input()
print(n + n[::-1])
