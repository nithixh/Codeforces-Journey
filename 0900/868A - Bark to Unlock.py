"""
Problem: 868A - Bark to Unlock
Rating: 900

Idea:
The password has only 2 characters. For it to appear as a substring
after joining two words, the first word must end with the first character
of the password and the second word must start with the second character.

Store the first and last characters of all words and check whether such
a pair exists.
"""

password=input()
n=int(input())
first=set()
last=set()
for _ in range(n):
    word=input()
    first.add(word[0])
    last.add(word[1])
if password[0] in last and password[1] in first:
    print("YES")
else:
    print("NO")
