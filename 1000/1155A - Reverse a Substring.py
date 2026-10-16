"""
Problem: 1155A - Reverse a Substring
Rating: 1000
Link: https://codeforces.com/problemset/problem/1155/A

Idea:
To make the string lexicographically smaller, find the first position
where a character is smaller than the character immediately before it.

If s[i] < s[i - 1], reversing these two adjacent characters makes
the string lexicographically smaller.

Print YES and their 1-based positions. If no such pair exists,
the string is already sorted in non-decreasing order, so print NO.
"""

n = int(input())
s = input()
for i in range(1, n):
    if s[i] < s[i - 1]:
        print("YES")
        print(i, i + 1)
        break
else:
    print("NO")
