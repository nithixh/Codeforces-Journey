"""
Problem: 17A - Noldbach problem
Rating: 1000
Link: https://codeforces.com/problemset/problem/17/A

Idea:
Generate all prime numbers from 2 to n.
For every pair of consecutive primes, calculate:
    candidate = prime1 + prime2 + 1

If candidate is also prime and <= n, increase the count.
Finally, if count >= k, print YES; otherwise, print NO.
"""

n, k = map(int, input().split())
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
primes = [i for i in range(2, n + 1) if is_prime[i]]
count = 0
for i in range(len(primes) - 1):
    candidate = primes[i] + primes[i + 1] + 1
    if candidate <= n and is_prime[candidate]:
        count += 1
print("YES" if count >= k else "NO")
