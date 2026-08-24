"""
Problem: 876A - Trip For Meal
Rating: 900
Link: https://codeforces.com/problemset/problem/876/A

Idea:
Winnie starts at Rabbit's house, so his first move can only be to Owl or
Eeyore. Therefore, the first move costs min(a,b).

After reaching Owl or Eeyore, he can always move along the shortest of the
three paths. So every remaining move costs min(a,b,c).

There are n-1 moves in total, hence the answer is:
min(a,b) + (n-2)*min(a,b,c)
"""

n=int(input())
a=int(input())
b=int(input())
c=int(input())

if n==1:
    print(0)
else:
    ans=min(a,b)+(n-2)*min(a,b,c)
    print(ans)
