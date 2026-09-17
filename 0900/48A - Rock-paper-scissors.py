"""
Problem: 48A - Rock-paper-scissors
Rating: 900
Link: https://codeforces.com/problemset/problem/48/A

Idea:
There are three possible gestures: rock, paper, and scissors.

A player wins only if their gesture beats both other players:
rock beats scissors, scissors beats paper, and paper beats rock.

If all three gestures are the same, or all three gestures are different,
there is no unique winner, so we print "?".

Otherwise, exactly one gesture appears twice. The player with the other
gesture is the only possible winner if their gesture beats the repeated
gesture.
"""

f = input()
m = input()
s = input()
moves = [f, m, s]
if moves.count("rock") == 2 and "paper" in moves:
    print("F" if f == "paper" else "M" if m == "paper" else "S")
elif moves.count("paper") == 2 and "scissors" in moves:
    print("F" if f == "scissors" else "M" if m == "scissors" else "S")
elif moves.count("scissors") == 2 and "rock" in moves:
    print("F" if f == "rock" else "M" if m == "rock" else "S")
else:
    print("?")
