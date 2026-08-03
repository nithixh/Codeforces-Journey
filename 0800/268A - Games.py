"""
Problem: 268A - Games
Rating: 800
Link: https://codeforces.com/problemset/problem/268/A

Idea:
A host team wears its guest uniform whenever its home uniform color matches the
guest uniform color of the visiting team. Compare the home color of every team
with the guest color of every other team and count all such matches.
"""

n = int(input())

teams = []
for _ in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))

ans = 0

for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:
            ans += 1

print(ans)
