"""
Problem: 980A - Links and Pearls
Rating: 900
Link: https://codeforces.com/problemset/problem/980/A

Idea:
Count the number of pearls ('o') and links ('-').

Since the necklace is circular, the links must be distributed
equally between all adjacent pearls.

Therefore:
- If there are no pearls, the answer is YES.
- Otherwise, the number of links must be divisible by
  the number of pearls.

Check this condition and print YES or NO.
"""

s = input()
pearls = s.count('o')
links = s.count('-')
if pearls == 0 or links % pearls == 0:
    print("YES")
else:
    print("NO")
