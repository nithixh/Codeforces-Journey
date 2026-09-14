"""
Problem: 137A - Postcards and photos
Rating: 900
Link: https://codeforces.com/problemset/problem/137/A

Idea:
We process the string from left to right and divide it into consecutive
groups of the same type (C or P).

For each group, Polycarpus can carry at most 5 items in one visit.
Therefore, a group of length x requires ceil(x / 5) visits.

We add this value for every consecutive group to get the minimum
number of visits.
"""

s = input()
ans = 0
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        ans += (count + 4) // 5
        count = 1
ans += (count + 4) // 5
print(ans)
