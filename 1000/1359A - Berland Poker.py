"""
Problem: 1359A - Berland Poker
Rating: 1000
Link: https://codeforces.com/problemset/problem/1359/A

Idea:
Each player gets n // k cards.

Give as many jokers as possible to the first player.
The maximum number of jokers they can get is min(m, n // k).

Distribute the remaining jokers as evenly as possible among the
other k - 1 players to minimize the maximum number any of them gets.

The maximum jokers another player can get is the ceiling of
remaining_jokers / (k - 1).

The answer is the first player's jokers minus the maximum jokers
another player can get.
"""

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    first = min(m, n // k)
    remaining = m - first
    other = (remaining + k - 2) // (k - 1)
    print(first - other)
