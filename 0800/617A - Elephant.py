"""
Problem: 617A - Elephant
Rating: 800
Link: https://codeforces.com/problemset/problem/617/A

Idea:
To minimize the number of steps, the elephant should always take the maximum
possible step size of 5. Count the number of complete 5-unit steps, and if
there is any remaining distance, one additional step is enough to cover it.
"""

n=int(input())
steps=n//5
if n%5:
    steps+=1
print(steps)
