"""
Problem: 975A - Aramic script
Rating: 900

Idea:
For each word, its root is simply the set of distinct letters in it.
So sort the distinct letters of every word and store them in a set.
The size of this set gives the number of different objects.
"""

n=int(input())
words=input().split()
st=set()
for word in words:
    root="".join(sorted(set(word)))
    st.add(root)
print(len(st))
