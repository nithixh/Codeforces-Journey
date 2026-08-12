"""
Problem: 653A - Bear and Three Balls
Rating: 900
Link: https://codeforces.com/problemset/problem/653/A

Idea:
Remove duplicate ball sizes and sort the remaining sizes. We need three
distinct sizes such that the difference between the smallest and largest is
at most 2. After sorting, such three sizes must appear as three consecutive
values differing by exactly 1, so check every group of three consecutive
elements in the sorted list.
"""

n=int(input())
balls=list(map(int,input().split()))
balls = list(set(balls))
balls.sort()
n=len(balls)
for i in range(n-2):
    curr=i
    for j in range(i+1,i+3):
        if balls[j]-balls[curr]!=1:
            break
        curr+=1
    else:
        print("YES")
        break
else:
    print("NO")
