"""
Problem: 443A - Anton and Letters
Rating: 800
Link: https://codeforces.com/problemset/problem/443/A

Idea:
Store all characters in a set to remove duplicate letters. Then count only the
lowercase letters in the set, ignoring the braces, commas, and spaces. The final
count is the number of distinct letters in Anton's set.
"""

s=input()
st=set(s)
ans=0
for i in st:
    if i.islower():
        ans+=1
print(ans)
