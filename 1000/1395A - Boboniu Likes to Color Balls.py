"""
Problem: 1395A - Boboniu Likes to Color Balls
Rating: 1000
Link: https://codeforces.com/problemset/problem/1395/A

Idea:
A palindrome can have at most one character with an odd frequency.

Count how many of r, g, b, and w are odd.
If at most one count is odd, print YES.

Otherwise, if r, g, and b are all positive, we can perform one
operation: decrease r, g, and b by 1 and increase w by 3.
This changes the parity of all four counts.

After this operation, check again whether at most one count is odd.
If so, print YES; otherwise, print NO.

If any of r, g, or b is zero, the operation cannot be performed.
"""

t = int(input())
for _ in range(t):
    r, g, b, w = map(int, input().split())
    odd = (r % 2) + (g % 2) + (b % 2) + (w % 2)
    if odd <= 1:
        print("Yes")
    elif r > 0 and g > 0 and b > 0:
        r -= 1
        g -= 1
        b -= 1
        w += 3
        odd = (r % 2) + (g % 2) + (b % 2) + (w % 2)
        if odd <= 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
