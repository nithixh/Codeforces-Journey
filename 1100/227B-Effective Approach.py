"""
Problem: 227B - Effective Approach
Rating: 1100
Link: https://codeforces.com/problemset/problem/227/B

Idea:
Store the position of each element using a dictionary.
Each query can then be answered in O(1) by using the
stored position instead of performing a linear search.
"""

n = int(input())
arr = list(map(int, input().split()))

# Store the 1-based position of every element
pos = {}
for i in range(n):
    pos[arr[i]] = i + 1

vasya = 0
petya = 0

m = int(input())
queries = list(map(int, input().split()))

# Calculate the number of comparisons for each query
for x in queries:
    else:
        vasya += pos[x]
        petya += n - pos[x] + 1

print(f"{vasya} {petya}")
