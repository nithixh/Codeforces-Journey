"""
Problem: 616A - Comparing Two Long Integers
Rating: 900
Link: https://codeforces.com/problemset/problem/616/A

Idea:
Leading zeroes do not affect the value of a number, so remove them from
both numbers first. If one number has more digits, it is larger.

If both have the same number of digits, compare them as strings. Since
they contain only digits and have equal length, lexicographical comparison
gives the correct numerical comparison.
"""

a=input().lstrip("0") or "0"
b=input().lstrip("0") or "0"

if len(a)<len(b):
    print("<")
elif len(a)>len(b):
    print(">")
elif a<b:
    print("<")
elif a>b:
    print(">")
else:
    print("=")
