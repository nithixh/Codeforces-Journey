"""
Problem: 58A - Chat room
Rating: 1000
Link: https://codeforces.com/problemset/problem/58/A

Idea:
We need to check whether "hello" can be formed as a subsequence of s.

Scan the string from left to right and keep track of the next character
we need from "hello".

Whenever the current character matches, move to the next character.
If all 5 characters are matched, print "YES"; otherwise print "NO".
"""

s = input()
target = "hello"
j = 0
for ch in s:
    if ch == target[j]:
        j += 1

        if j == 5:
            break
if j == 5:
    print("YES")
else:
    print("NO")
