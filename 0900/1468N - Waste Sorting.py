"""
Problem: 1468N - Waste Sorting
Rating: 900
Link: https://codeforces.com/problemset/problem/1468/N

Idea:
First place the fixed types of waste into their respective containers:
paper into container 1, plastic into container 2, and general waste into
container 3. If any of these containers exceeds its capacity, the answer is NO.
Container 3 is shared by general waste, partially-paper waste, and
partially-plastic waste, so we should keep as much space as possible in it.
Therefore, put partially-paper waste into the remaining space of container 1
first, and put partially-plastic waste into the remaining space of container 2
first. Any leftover items are then placed into container 3.
If all items can be placed, print YES; otherwise, print NO.
"""

t=int(input())
for _ in range(t):
    c1,c2,c3=map(int,input().split())
    a1,a2,a3,a4,a5=map(int,input().split())
    c1=c1-a1
    a1=0
    c2=c2-a2
    a2=0
    c3=c3-a3
    a3=0
    if c1<0 or c2<0 or c3<0:
        print("NO")
        continue
    if a4<=c1:
        c1=c1-a4
        a4=0
    else:
        a4=a4-c1
        c1=0
    if a4<=c3:
        c3=c3-a4
        a4=0
    else:
        print("NO")
        continue
    if a5<=c2:
        c2=c2-a5
        a5=0
    else:
        a5=a5-c2
        c2=0
    if a5<=c3:
        c3=c3-a5
        a5=0
    else:
        print("NO")
        continue
    print("YES")
        
