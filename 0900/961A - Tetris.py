"""
Problem: 961A - Tetris
Rating: 900
Link: https://codeforces.com/problemset/problem/961/A

Idea:
Count how many squares appear in each column.

Whenever every column has at least one square, one complete
row is removed and we get one point.

Therefore, the total number of points equals the minimum
number of squares among all columns.

Print the minimum column count.
"""

n, m = map(int, input().split())
c = list(map(int, input().split()))
count = [0] * n
for x in c:
    count[x - 1] += 1
print(min(count))
