"""
Problem: 237A - Free Cash
Rating: 1000
Link: https://codeforces.com/problemset/problem/237/A

Idea:
The minimum number of cash registers needed is the maximum number
of customers arriving at exactly the same time.

Use a dictionary to count how many customers arrive at each time.
For every arrival time (hour, minute), increase its frequency.

Finally, print the maximum frequency in the dictionary.
"""

n = int(input())
freq = {}
for _ in range(n):
    h, m = map(int, input().split())
    time = (h, m)
    freq[time] = freq.get(time, 0) + 1
print(max(freq.values()))
