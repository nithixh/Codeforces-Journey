"""
Problem: 765A - Neverending competitions
Rating: 900
Link: https://codeforces.com/problemset/problem/765/A

Idea:
Jinotega starts the year at his home airport and always travels between
his home and competition locations. Therefore, every time he leaves home,
he must eventually return home.

We count how many flights start from the home airport and how many arrive
at the home airport. If both counts are equal, all trips are complete and
Jinotega is at home. Otherwise, he is currently at a competition.
"""

n = int(input())
home = input()

home_departures = 0
home_arrivals = 0

for _ in range(n):
    flight = input()
    departure, arrival = flight.split("->")

    if departure == home:
        home_departures += 1

    if arrival == home:
        home_arrivals += 1

if home_departures == home_arrivals:
    print("home")
else:
    print("contest")
