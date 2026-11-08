"""
Problem: 893A - Chess For Three
Rating: 900
Link: https://codeforces.com/problemset/problem/893/A

Idea:
Initially, Alex (1) and Bob (2) play, while Carl (3) watches.

For every game:
- The winner must be one of the two players currently playing.
- The winner continues playing.
- The loser becomes the spectator, replacing the previous spectator.

If the spectator wins a game, the given sequence is impossible.

Simulate the games by keeping track of the current spectator.
"""

n = int(input())
spectator = 3
possible = True
for _ in range(n):
    winner = int(input())
    if winner == spectator:
        possible = False
        break
    spectator = 6 - spectator - winner
print("YES" if possible else "NO")
