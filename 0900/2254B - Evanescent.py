"""
Problem: 2254B - Evanescent
Rating: 900
Link: https://codeforces.com/problemset/problem/2254/B

Idea:
First find the compressed length by counting the number of different
consecutive blocks.

Deleting a character can remove a whole block only when that block has
length 1. If an internal block has length 1 and its neighboring blocks
contain the same character, deleting it merges those two blocks, reducing
the compressed length by 2.

Otherwise, deleting an internal block of length 1 only reduces the length
by 1. If there is no such block, the compressed length cannot be reduced.
"""

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    
    blocks=[]
    i=0
    
    while i<n:
        j=i
        while j<n and s[j]==s[i]:
            j+=1
        blocks.append((s[i],j-i))
        i=j
    
    ans=len(blocks)
    
    for i in range(1,len(blocks)-1):
        if blocks[i][1]==1 and blocks[i-1][0]==blocks[i+1][0]:
            ans-=2
            break
    else:
        for i in range(1,len(blocks)-1):
            if blocks[i][1]==1:
                ans-=1
                break
    
    print(ans)
