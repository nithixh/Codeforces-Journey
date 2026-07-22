"""
Problem: 1509B - TMT Document
Rating: 1100
Link: https://codeforces.com/problemset/problem/1509/B

Idea:
A valid document must contain exactly twice as many 'T's as 'M's, since every
subsequence is "TMT". Then, scan the string from left to right to ensure that
every 'M' has a preceding 'T'. Repeat the check from right to left to ensure
every 'M' also has a succeeding 'T'. If both conditions hold, the document is
valid.
"""

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    T=M=0
    for c in s:
        if c=='T':
            T+=1
        else:
            M+=1
    if T!=2*M:
        print("NO")
        continue
    ok=True
    tcnt=mcnt=0
    for c in s:
        if c=='T':
            tcnt+=1
        else:
            mcnt+=1
        if mcnt>tcnt:
            ok=False
            break
    tcnt=mcnt=0
    if ok:
        for i in range(n-1,-1,-1):
            if s[i]=='T':
                tcnt+=1
            else:
                mcnt+=1
            if mcnt>tcnt:
                ok=False
                break
    if ok:
        print("YES")
    else:
        print("NO")
