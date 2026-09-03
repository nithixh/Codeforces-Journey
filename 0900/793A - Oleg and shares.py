"""
Problem: 793A - Oleg and shares
Rating: 900
Link: https://codeforces.com/problemset/problem/793/A

Idea:
Every second, exactly one price decreases by k. Therefore, the remainder
of every price when divided by k never changes.

For all prices to become equal, they must have the same remainder modulo k.
If they don't, it is impossible.

If they can become equal, the final price must be the minimum initial price,
because prices can only decrease and can never increase.

For every price ai, we need (ai - minimum) / k decreases.
The total number of decreases is the minimum number of seconds needed.
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
for x in a:
    if x % k != a[0] % k:
        print(-1)
        break
else:
    mn = min(a)
    ans = 0
    for x in a:
        ans += (x - mn) // k
    print(ans)
