"""
28 Implement StrStr()
1) first range()  if b has two characters, when we loop a, we can ditch the last a few charters of a if that part number of characters < len(b)
    ex: a = l e e t  c o d e
        b = l e e t  o

        we dont have to include o d e, since 3 < 5

        by doing so, use len(a) - len(b) + 1, so you will loop characters : l e e t c

2) comparison , compare the length of len(b)




"""

def strStr(a, b):
    for i in range( len(a) - len(b) + 1):
        if a[i : i + len(b)] == b:
            return i

    return  -1


a = "sadbutsad"
b = "sad"

print(strStr(a,b))

