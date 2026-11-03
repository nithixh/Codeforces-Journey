"""
Problem: 863A - Quasi-palindrome
Rating: 900
Link: https://codeforces.com/problemset/problem/863/A

Idea:
A number is quasi-palindromic if removing its trailing zeros
makes it a palindrome.

Convert the number into a string and remove all trailing zeros.
Then check whether the remaining string is equal to its reverse.

If they are equal, print YES; otherwise, print NO.
"""

s = input()
s = s.rstrip('0')
if s == s[::-1]:
    print("YES")
else:
    print("NO")
