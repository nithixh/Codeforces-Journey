"""
Problem: 847G - University Classes
Rating: 900
Link: https://codeforces.com/problemset/problem/847/G

Idea:
For each of the 7 time slots, count how many groups have a class
in that slot.

Since one room can hold only one group at a time, the number of rooms
needed is the maximum number of groups having a class in any single
time slot.

Therefore, count the 1s in each column and print the maximum.
"""

n = int(input())
schedule = []
for _ in range(n):
    schedule.append(input())
ans = 0
for j in range(7):
    count = 0
    for i in range(n):
        if schedule[i][j] == '1':
            count += 1
    ans = max(ans, count)
print(ans)
