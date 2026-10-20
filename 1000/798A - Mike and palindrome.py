"""
Problem: 798A - Mike and palindrome
Rating: 1000
Link: https://codeforces.com/problemset/problem/798/A

Idea:
Compare characters from the beginning and end of the string.

Count how many pairs of characters are different.

If exactly one pair differs, changing one character can make the string
a palindrome, so print YES.

If no pairs differ, the string is already a palindrome.
We can change exactly one character and keep it a palindrome only if
the string length is odd, by changing its middle character.

If more than one pair differs, one character change is not enough,
so print NO.
"""

s=input()
n=len(s)
l=0
r=n-1
c=0
while l<r:
    if s[l]!=s[r]:
        c+=1
    l+=1
    r-=1
if c==1:
    print("YES")
elif c==0:
    if n%2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
