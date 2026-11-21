"""
Problem: 45A - Codecraft III
Rating: 900
Link: https://codeforces.com/problemset/problem/45/A

Idea:
Store all 12 months in their calendar order.

Find the index of the current month and add k to it.
Since the calendar repeats every 12 months, use % 12
to get the correct month index.

Print the month at that index.
"""

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
s = input()
k = int(input())
index = months.index(s)
print(months[(index + k) % 12])
