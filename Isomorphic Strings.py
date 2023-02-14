"""

205. Isomorphic Strings

dic doesnt allow duplicate values

create two dic for comparsion
use zip to pair two strings
if the dic is empty , we add it
if not empty we compare them by get() values

"""

def isIsomorphic(s, t):
    mappingS, mappingT = {}, {}

    for x, j in zip(s, t):
        if (x not in mappingS) and (j not in mappingT):
            mappingS[x] = j
            mappingT[j] = x
        elif mappingS.get(x) != j or mappingT.get(j) != x:
            return False

    return True


s = "egg"
t = "abr"

print(isIsomorphic(s, t))


"""




"""




