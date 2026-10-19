"""
Problem: 1485A - Add and Divide
Rating: 1000
Link: https://codeforces.com/problemset/problem/1485/A

Idea:
We need to make a equal to 0 using the minimum number of operations.

If b = 1, division does not reduce a, so first increase b.
Try different numbers of increments to b, starting from 0.

For each possibility, repeatedly divide a by the updated b until
a becomes 0, counting the operations.

Keep track of the minimum total operations among all possibilities.
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = a + 1
    for inc in range(32):
        if b + inc == 1:
            continue
        x = a
        ops = inc
        while x > 0:
            x //= (b + inc)
            ops += 1
        ans = min(ans, ops)
    print(ans)
