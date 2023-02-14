"""

217. Contains Duplicate


"""
def containsDuplicate(li):
    dic = {}

    for i in range(len(li)):
        if li[i] in dic:
            return True
        else:
            dic[li[i]] = i

    return False



nums = [1,2,3,1]
print(containsDuplicate(nums))
"""
create a empty dic

iterate each element in the list
if it is in the dic return true
else add it 
"""

