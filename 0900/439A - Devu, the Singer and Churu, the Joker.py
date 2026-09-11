"""
Problem: 439A - Devu, the Singer and Churu, the Joker
Rating: 900
Link: https://codeforces.com/problemset/problem/439/A

Idea:
Devu needs sum(t) minutes to sing all the songs.
He also needs 10 minutes of rest after every song except the last one.
Therefore, the minimum time required to conduct the event is:
sum(t) + 10 * (n - 1)
If this is greater than d, it is impossible.
The 10-minute rest periods can be used by Churu to tell jokes.
So the total time available for Churu is simply d - sum(t).
Each joke takes 5 minutes, so the maximum number of jokes is
(d - sum(t)) // 5.
"""

n, d = map(int, input().split())
t = list(map(int, input().split()))
song_time = sum(t)
if song_time + 10 * (n - 1) > d:
    print(-1)
else:
    print((d - song_time) // 5)
