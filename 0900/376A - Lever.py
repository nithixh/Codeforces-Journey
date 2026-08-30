"""
Problem: 376A - Lever
Rating: 900
Link: https://codeforces.com/problemset/problem/376/A

Idea:
Find the position of the pivot '^'. For every weight, calculate its torque
using weight * distance from the pivot. Add the torques on the left and
right separately. If both torques are equal, the lever is balanced.
Otherwise, the side with the larger torque is the direction in which the
lever tilts.
"""

s=input()
p=s.index('^')

left=0
right=0

for i in range(len(s)):
    if s[i].isdigit():
        w=int(s[i])
        if i<p:
            left+=w*(p-i)
        else:
            right+=w*(i-p)

if left==right:
    print("balance")
elif left>right:
    print("left")
else:
    print("right")
