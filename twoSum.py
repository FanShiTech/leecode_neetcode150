"""
Leecode #1 two sum


"""

def TwoSum(li, target):
    dic = {}

    for i in range(len(li)):
        ans = target - li[i]

        if ans in dic:
            return [i, dic[ans]]
        else:
            dic[li[i]] = i




nums = [2, 7, 11, 15]
target = 9

print(TwoSum(nums,target))

"""
create a dictionary

for everything in the range len list
get a difference by using target - the current value

if it is in the dic, return the index 
else, add it to the dic


"""