"""
Problem: 834A - The Useless Toy
Rating: 900
Link: https://codeforces.com/problemset/problem/834/A

Idea:
The spinner has 4 positions in clockwise order:
v, <, ^, >

Find the index of the starting and ending positions.

After n rotations:
- Clockwise position = (start + n) % 4
- Counter-clockwise position = (start - n) % 4

If both directions lead to the same ending position,
print "undefined".

Otherwise, check which direction reaches the ending position
and print "cw" or "ccw".
"""

s, e = input().split()
n = int(input())
positions = ['v', '<', '^', '>']
start = positions.index(s)
end = positions.index(e)
cw = (start + n) % 4
ccw = (start - n) % 4
if cw == ccw:
    print("undefined")
elif cw == end:
    print("cw")
else:
    print("ccw")
