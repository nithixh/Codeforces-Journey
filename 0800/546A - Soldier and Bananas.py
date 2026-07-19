"""
Problem: 546A - Soldier and Bananas
Rating: 800
Link: https://codeforces.com/problemset/problem/546/A

Idea:
The cost of the bananas forms an arithmetic progression with first term k,
last term w × k, and w terms. Use the sum of an AP formula to calculate the
total cost. If the total cost is greater than the money the soldier has,
print the amount he needs to borrow; otherwise, print 0.
"""

k,n,w=map(int,input().split())
tot = (w/2)*(k+w*k)
if tot<=n:
    print(0)
else:
    needed=(tot-n)
    print(int(needed))
