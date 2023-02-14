

"""

66 add one

get the len first
iterate the list, and go to the last element first
if the value at each position is 9 , change it to 0
if not, increase 1
if all the digit is 9 , return [1] + digit

"""

def addOne(li):
    n = len(li)

    for i in range(n):
        idx = n - 1 - i
        if li[idx] == 9:
            li[idx] = 0
        else:
            li[idx] += 1
            return li
    return [1] + li




num = [1,2,3]
print(addOne(num))