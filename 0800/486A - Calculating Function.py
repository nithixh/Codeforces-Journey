"""
Problem: 486A - Calculating Function
Rating: 800
Link: https://codeforces.com/problemset/problem/486/A

Idea:
Separate the odd and even numbers from 1 to n. Compute the sum of odd numbers
and the sum of even numbers using the arithmetic progression (AP) sum formula.
Since the function subtracts odd numbers and adds even numbers, the answer is
the difference between the even sum and the odd sum.
"""

n=int(input())
evenum=oddnum=n
evecnt=n//2
oddcnt=n//2
if n%2:
    evenum=n-1
    oddcnt+=1
else:
    oddnum=n-1
odd=(oddcnt)*(1+oddnum)//2
even=(evecnt)*(2+evenum)//2
print(even-odd)
