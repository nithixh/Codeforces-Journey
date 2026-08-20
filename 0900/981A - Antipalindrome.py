"""
Problem: 981A - Antipalindrome
Rating: 900

Idea:
If all characters are the same, every substring is a palindrome, so the
answer is 0.

Otherwise, if the whole string is not a palindrome, the answer is its
length. If it is a palindrome, removing one character from either end
gives the longest possible non-palindromic substring, so the answer is
n-1.
"""

s=input()
n=len(s)
if len(set(s))==1:
    print(0)
elif s!=s[::-1]:
    print(n)
else:
    print(n-1)
