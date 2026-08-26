"""
Problem: 916A - Jamie and Alarm Snooze
Rating: 900
Link: https://codeforces.com/problemset/problem/916/A

Idea:
Convert the wake-up time into total minutes. Then keep going backwards by
x minutes until we reach a lucky time, i.e. a time whose hour or minute
contains the digit '7'. The number of steps is the minimum number of times
Jamie needs to press the snooze button.
"""

x=int(input())
h,m=map(int,input().split())

time=h*60+m
ans=0

while True:
    hh=time//60
    mm=time%60
    if '7' in str(hh) or '7' in str(mm):
        print(ans)
        break
    time=(time-x)%1440
    ans+=1
