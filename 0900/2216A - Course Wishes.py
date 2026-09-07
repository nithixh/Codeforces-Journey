"""
Problem: 2216A - Course Wishes
Rating: 900
Link: https://codeforces.com/problemset/problem/2216/A

Idea:
We need to move every course to level k+1, and every move increases its
level by 1.

To avoid violating capacity limits, process the levels from k down to 1.
Before moving courses from level i to i+1, all courses already at level
i+1 have been moved further up, so there is enough space for the courses
from level i.

For every course, perform k+1-bi operations and store its index. Since
n<=50 and k<=20, the total number of operations is at most 1000.
"""

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    ans=[]
    
    for level in range(k,0,-1):
        for i in range(n):
            if b[i]==level:
                while b[i]<k+1:
                    b[i]+=1
                    ans.append(i+1)
    
    print(len(ans))
    if ans:
        print(*ans)
