"""
Problem: 1251A - Broken Keyboard
Rating: 1000
Link: https://codeforces.com/problemset/problem/1251/A

Idea:
A malfunctioning key always produces exactly 2 copies of a
character, while a working key produces 1 copy.

Therefore, check consecutive groups of identical characters.
If a group's length is odd, that character's key must be working.

Store such characters in a set to avoid duplicates.
Finally, sort the set and print the result.
"""

t = int(input())
for _ in range(t):
    s = input()
    working = set()
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        if (j - i) % 2 == 1:
            working.add(s[i])
        i = j
    print("".join(sorted(working)))
