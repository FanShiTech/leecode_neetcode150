"""

14 longest common prefix

TC 0(N)
SC O(1)

   f l o w e r
   f l o w
   f l i g h t

"""

def longestCommonPrefix(li):
    res = ""
    for i in range(len(li[0])):    # for i in (flower)  6
        for x in li:                # x is each substring
            if i == len(x) or x[i] != li[0][i]:  # ex, since len(flow) < len(flower) , if i == len(x) , i is out of the boundry or if character x[i] != the chacarer in flower
                return res
        res += li[0][i]



s = ["flower","flow","flight"]

print(longestCommonPrefix(s))