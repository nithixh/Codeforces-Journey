"""
Problem: 670A - Holidays
Rating: 900
Link: https://codeforces.com/problemset/problem/670/A

Idea:
Every complete 7-day week contains exactly 2 days off.

For the remaining days, the minimum number of days off is obtained by
placing the 2 days off outside the remaining part as much as possible,
while the maximum is obtained by placing as many days off as possible
inside it.

So:
minimum = full_weeks*2 + max(0,remainder-5)
maximum = full_weeks*2 + min(2,remainder)
"""

n=int(input())
weeks=n//7
rem=n%7
mn=weeks*2+max(0,rem-5)
mx=weeks*2+min(2,rem)
print(mn,mx)
