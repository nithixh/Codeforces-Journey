"""
Problem: 1150B - Tiling Challenge
Rating: 900
Link: https://codeforces.com/problemset/problem/1150/B

Idea:
Each piece consists of 5 cells in a plus (+) shape.

Traverse the board from top to bottom and left to right.
Whenever we find a free cell '.', it must be the top cell
of a new piece.

Check whether these 5 positions are free:
    (i, j)       - Top
    (i+1, j)     - Center
    (i+1, j-1)   - Left
    (i+1, j+1)   - Right
    (i+2, j)     - Bottom

If all 5 cells are free, mark them as occupied '#'.
Otherwise, print NO.

If the entire board is processed successfully, print YES.
"""

n = int(input())
board = [list(input()) for _ in range(n)]
possible = True
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            if (i + 2 >= n or j - 1 < 0 or j + 1 >= n or
                board[i + 1][j] != '.' or
                board[i + 1][j - 1] != '.' or
                board[i + 1][j + 1] != '.' or
                board[i + 2][j] != '.'):
                possible = False
                break
            board[i][j] = '#'
            board[i + 1][j] = '#'
            board[i + 1][j - 1] = '#'
            board[i + 1][j + 1] = '#'
            board[i + 2][j] = '#'
    if not possible:
        break
print("YES" if possible else "NO")
