"""
Problem: 441A - Valera and Antique Items
Rating: 1000
Link: https://codeforces.com/problemset/problem/441/A

Idea:
Valera can buy an item from a seller if its current price
is strictly less than the money he has (v).

For each seller:
1. Read the number of items and their prices.
2. Find the minimum price among those items.
3. If the minimum price is less than v, add the seller's
   1-based index to the answer.

Finally, print the number of possible sellers and their
indices in increasing order.
"""

n, v = map(int, input().split())
ans = []
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    k = data[0]
    prices = data[1:]
    if min(prices) < v:
        ans.append(i)
print(len(ans))
if ans:
    print(*ans)
