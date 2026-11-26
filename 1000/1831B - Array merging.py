"""
Problem: 1831B - Array merging
Rating: 1000
Link: https://codeforces.com/problemset/problem/1831/B

Idea:
For each value, find its longest consecutive segment in
array a and its longest consecutive segment in array b.

Since we can choose the order of merging, we can place
these two segments next to each other in the merged array.

Therefore, for each value x:
    length = max_run_a[x] + max_run_b[x]

The answer is the maximum such length among all values.

Repeat this for every test case.
"""

def get_best(arr, n):
    best = [0] * (2 * n + 1)
    current = 0
    previous = -1
    for x in arr:
        if x == previous:
            current += 1
        else:
            current = 1
        best[x] = max(best[x], current)
        previous = x
    return best


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    best_a = get_best(a, n)
    best_b = get_best(b, n)
    ans = 0
    for x in range(1, 2 * n + 1):
        ans = max(ans, best_a[x] + best_b[x])
    print(ans)
