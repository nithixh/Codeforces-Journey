"""
Problem: 268B - Buttons
Rating: 1000
Link: https://codeforces.com/problemset/problem/268/B

Idea:
For the i-th button in the correct sequence, there can be (n - i)
wrong guesses in the worst case.

Each wrong guess requires pressing the already correct i buttons again,
so it costs (n - i) * i presses.

Finally, all n buttons must be pressed correctly once.

Therefore, the answer is:
n + sum((n - i) * i) for i from 1 to n.
"""

n = int(input())
ans = n
for i in range(1, n + 1):
    ans += (n - i) * i
print(ans)
