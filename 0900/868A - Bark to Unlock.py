"""
Problem: 868A - Bark to Unlock
Rating: 900

Idea:
The password can either be one of the known words, or it can be formed by
joining two words.

For two words to form the password across their boundary, the first word
must end with the first character of the password and the second word must
start with the second character.
"""

password=input()
n=int(input())
first=set()
last=set()
words=set()
for _ in range(n):
    word=input()
    words.add(word)
    first.add(word[0])
    last.add(word[1])
if password in words or (password[0] in last and password[1] in first):
    print("YES")
else:
    print("NO")
