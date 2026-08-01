"""
Problem: 520A - Pangram
Rating: 800
Link: https://codeforces.com/problemset/problem/520/A

Idea:
Convert the string to lowercase so that uppercase and lowercase letters are
treated the same. If the set of characters contains all 26 letters of the
English alphabet, the string is a pangram; otherwise, it is not.
"""

n=int(input())
s=input()
s=s.lower()
if len(set(s))==26:
    print("YES")
else:
    print("NO")
