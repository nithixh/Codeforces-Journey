"""
Problem: 194A - Exams
Rating: 900
Link: https://codeforces.com/problemset/problem/194/A

Idea:
To minimize the number of failed exams (marks of 2),
we should first assign 3 marks to every exam.

The initial total is 3*n.

If 3*n <= k, we can increase some marks to reach k
without giving anyone a 2. So the answer is 0.

Otherwise, each mark of 2 reduces the total by 1.
Therefore, we need at least 3*n-k exams with mark 2.

Answer = max(0, 3*n-k).
"""

n, k = map(int, input().split())
print(max(0, 3 * n - k))
