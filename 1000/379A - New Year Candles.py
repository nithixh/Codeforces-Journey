"""
Problem: 379A - New Year Candles
Rating: 1000
Link: https://codeforces.com/problemset/problem/379/A

Idea:
Initially, Vasily has a candles, and each candle gives 1 hour of light.

After a candle is used, it becomes one burnt-out candle.
Whenever he has b burnt-out candles, he can exchange them for 1 new candle.

Keep track of the total hours in ans and the remaining burnt-out candles
in rem. Each time new candles are obtained, add them back to a and repeat.

The process stops when there are no candles left to burn.
"""

a,b=map(int,input().split())
ans=0
rem=0
while a>=1:
    ans+=a
    rem+=a
    a=rem//b
    rem=rem%b
print(ans)
