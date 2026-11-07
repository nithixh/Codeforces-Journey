"""
Problem: 373A - Collecting Beats is Fun
Rating: 900
Link: https://codeforces.com/problemset/problem/373/A

Idea:
There are two hands, and each hand can press at most k panels
at the same time. Therefore, he can press at most 2*k panels
for each digit.

Count how many times each digit (1 to 9) appears.
If any digit appears more than 2*k times, print NO.
Otherwise, print YES.

Ignore the '.' characters because those panels don't need
to be pressed.
"""

k = int(input())
count = {}
for _ in range(4):
    s = input()
    for c in s:
        if c != '.':
            count[c] = count.get(c, 0) + 1
possible = True
for c in count:
    if count[c] > 2 * k:
        possible = False
        break
print("YES" if possible else "NO")
