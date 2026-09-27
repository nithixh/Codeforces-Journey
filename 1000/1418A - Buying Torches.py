"""
Problem: 1418A - Buying Torches
Rating: 1000
Link: https://codeforces.com/problemset/problem/1418/A

Idea:
To make k torches, we need k coal and k sticks.
Each coal costs y sticks, so we need a total of:
k * y + k sticks.
Initially, we have 1 stick. Each stick trade gives a net gain of
x - 1 sticks.
Therefore, the number of stick trades needed is:
ceil((k * y + k - 1) / (x - 1))
We also need exactly k coal trades, one for each torch.

So the answer is:
stick trades + k
"""
 
t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    stick_trades = (k * y + k - 2 + x - 1) // (x - 1)
    print(stick_trades + k)
