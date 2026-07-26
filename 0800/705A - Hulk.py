"""
Problem: 705A - Hulk
Rating: 800
Link: https://codeforces.com/problemset/problem/705/A

Idea:
Start with "I hate" for the first layer. For each remaining layer, alternate
between "I love" and "I hate" based on whether the layer number is even or odd,
joining each feeling with "that". Finally, add "it" to complete the sentence.
"""

n=int(input())
ans="I hate"
for i in range(2,n+1):
    if i%2:
        ans+=" that I hate"
    else:
        ans+=" that I love"
ans+=" it"
print(ans)
