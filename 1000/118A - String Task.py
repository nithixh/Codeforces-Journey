"""
Problem: 118A - String Task
Rating: 1000
Link: https://codeforces.com/problemset/problem/118/A

Idea:
Remove all vowels from the string.

For every remaining character (consonant), add a "." before it.
Finally, convert the entire result to lowercase.

The vowels in this problem are a, o, y, e, u, i in both
uppercase and lowercase forms.
"""

s=input()
vowels={'a','A','e','E','i','I','o','O','u','U','y','Y'}
#Remove Vowels and add . before every consonant
news=""
for i in s:
    if i not in vowels:
        news+=("."+i)
#Upper -> Lower
news=news.lower()
print(news)
