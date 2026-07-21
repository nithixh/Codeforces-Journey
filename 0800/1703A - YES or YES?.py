"""
Problem: 1703A - YES or YES?
Rating: 800
Link: https://codeforces.com/problemset/problem/1703/A

Idea:
Convert the given string to lowercase so that the comparison becomes
case-insensitive. If the resulting string is "yes", print "YES";
otherwise, print "NO".
"""

t=int(input())
for _ in range(t):
    s=input()
    s=s.lower()
    if s=='yes':
        print("YES")
    else:
        print("NO")
