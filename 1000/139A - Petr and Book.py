"""
Problem: 139A - Petr and Book
Rating: 1000
Link: https://codeforces.com/problemset/problem/139/A

Idea:
Petr follows the same 7-day reading schedule every week. First, skip all the
complete weeks by calculating how many pages are read in one week. Then, simulate
the remaining days of the next week until the total pages read becomes at least n.
The day on which this happens is the answer.
"""

n=int(input())
pages=list(map(int,input().split()))
s=sum(pages)
week=n//s
read=s*week
if read==n:
    read=n-s
ans=0
for i in range(7):
    read+=pages[i]
    if read>=n:
        ans=i+1
        break
print(ans)
