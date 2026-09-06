"""
Problem: 747B - Mammoth's Genome Decoding
Rating: 900
Link: https://codeforces.com/problemset/problem/747/B

Idea:
Each of the four nucleotides must appear exactly n/4 times in the final string.
First count how many times A, C, G and T already occur.

The remaining question marks have to fill the missing occurrences of each
nucleotide. If n is not divisible by 4, or any nucleotide already appears
more than n/4 times, it is impossible.

Otherwise, replace the question marks with the required nucleotides.
"""

n=int(input())
s=input()
chars="ACGT"
need=n//4
cnt={i:s.count(i) for i in chars}

if n%4!=0 or any(cnt[i]>need for i in chars):
    print("===")
else:
    s=list(s)
    ans=[]
    for i in chars:
        ans.extend([i]*(need-cnt[i]))
    j=0
    for i in range(n):
        if s[i]=="?":
            s[i]=ans[j]
            j+=1
    print("".join(s))
