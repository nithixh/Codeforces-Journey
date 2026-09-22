"""
Problem: 43A - Football
Rating: 1000
Link: https://codeforces.com/problemset/problem/43/A

Idea:
Count how many goals each team scored using a frequency dictionary.

After counting all the teams, find the maximum number of goals scored.
The team with this maximum frequency is the winning team.

Since the problem guarantees that there are at most two teams and
the match did not end in a tie, there will be exactly one winner.
"""

from collections import defaultdict
n=int(input())
freq=defaultdict(int)
for i in range(n):
    freq[input()]+=1
mx=max(freq.values())
for i in freq:
    if freq[i]==mx:
        print(i)
        break
