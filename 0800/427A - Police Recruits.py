"""
Problem: 427A - Police Recruits
Rating: 800
Link: https://codeforces.com/problemset/problem/427/A

Idea:
Maintain the number of currently available police officers. Whenever recruits
arrive, add them to the available count. When a crime occurs, use one available
officer if possible; otherwise, the crime goes untreated. Count the number of
untreated crimes.
"""

n = int(input())
events = list(map(int, input().split()))

officers = 0
untreated = 0

for event in events:
    if event == -1:
        if officers > 0:
            officers -= 1
        else:
            untreated += 1
    else:
        officers += event

print(untreated)
