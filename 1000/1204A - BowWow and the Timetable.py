"""
Problem: 1204A - BowWow and the Timetable
Rating: 1000
Link: https://codeforces.com/problemset/problem/1204/A

Idea:
Trains depart at times 1, 4, 16, 64, and so on.
Their binary representations are 1 followed by an even number of zeros.

Start with len(s) // 2 as the answer.

If the binary string has odd length and contains a '1' after
the first character, increase the answer by 1.

This correctly counts the powers of 4 strictly smaller than s.
"""

s = input()
ans = len(s) // 2
if len(s) % 2 == 1 and '1' in s[1:]:
    ans += 1
print(ans)
