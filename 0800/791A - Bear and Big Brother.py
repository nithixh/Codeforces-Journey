"""
Problem: 791A - Bear and Big Brother
Rating: 800
Link: https://codeforces.com/problemset/problem/791/A

Idea:
Simulate the bears' growth year by year. In each year, Limak's weight is
tripled while Bob's weight is doubled. Count the number of years until
Limak's weight becomes strictly greater than Bob's.
"""

a,b=map(int,input().split())
c=0
while True:
    c+=1
    a=a*3
    b=b*2
    if a>b:
        print(c)
        break
