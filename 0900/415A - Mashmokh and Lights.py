"""
Problem: 415A - Mashmokh and Lights
Rating: 900
Link: https://codeforces.com/problemset/problem/415/A

Idea:
Initially, all lights are ON (represented by 0).

When button b is pressed, it turns OFF every light from
position b to n that is still ON.

Traverse the buttons in the given order.
For each button, visit all positions from b to n:
- If a light is still ON, assign the current button index.
- Otherwise, leave its previous value unchanged.

The final array contains the button that turned OFF each light.
"""

n, m = map(int, input().split())
b = list(map(int, input().split()))
ans = [0] * n
for x in b:
    for i in range(x - 1, n):
        if ans[i] == 0:
            ans[i] = x
print(*ans)
