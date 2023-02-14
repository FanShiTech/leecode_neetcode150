"""

202 happy number

create a set() to store the number that i've not visited
while n is not in the set()
add()
if n == 1, we return true, otherwise, the n is in the circle, or n is not 1 , return false

determine n, need a helper function. helper function return the sumofn

n -> n % 10 and n // 10


"""


def isHappy(n):
    visit = set()

    while n not in visit:
        visit.add(n)
        n = sumOfSquare(n)
        if n == 1:
            return True
    return False


def sumOfSquare(n):
    outPut = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        outPut += digit
        n = n // 10
    return outPut


print(isHappy(12))