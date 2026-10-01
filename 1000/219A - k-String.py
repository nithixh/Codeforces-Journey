"""
Problem: 219A - k-String
Rating: 1000
Link: https://codeforces.com/problemset/problem/219/A

Idea:
For the string to be a k-string, every character must appear a number
of times divisible by k.

If any character's frequency is not divisible by k, it is impossible,
so print -1.

Otherwise, create one part of the string using frequency // k copies
of each character, then repeat this part k times.
"""

k = int(input())
s = input()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in freq:
    if freq[ch] % k != 0:
        print(-1)
        break
else:
    part = ""

    for ch in freq:
        part += ch * (freq[ch] // k)

    print(part * k)
