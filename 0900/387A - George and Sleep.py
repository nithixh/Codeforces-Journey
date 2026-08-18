"""
Problem: 387A - George and Sleep
Rating: 900

Idea:
Convert both times into minutes. George's sleeping time is subtracted from
the current time. If the result becomes negative, add 24 hours since he may
have gone to bed yesterday.
"""

s=input()
t=input()

sh,sm=map(int,s.split(":"))
th,tm=map(int,t.split(":"))

cur=sh*60+sm
sleep=th*60+tm

ans=cur-sleep

if ans<0:
    ans+=24*60

h=ans//60
m=ans%60

print(f"{h:02d}:{m:02d}")
