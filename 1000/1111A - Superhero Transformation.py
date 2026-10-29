"""
Problem: 1111A - Superhero Transformation
Rating: 1000
Link: https://codeforces.com/problemset/problem/1111/A

Idea:
Two strings can be transformed into each other if:
1. Their lengths are equal.
2. Characters at corresponding positions are both vowels
   or both consonants.

Vowels are a, e, i, o, u.
Check every corresponding character and print Yes if all
positions have matching types; otherwise, print No.
"""

s = input()
t = input()
vowels = "aeiou"
if len(s) != len(t):
    print("No")
else:
    possible = True
    for i in range(len(s)):
        if (s[i] in vowels) != (t[i] in vowels):
            possible = False
            break
    print("Yes" if possible else "No")
