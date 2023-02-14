"""

67 add binary
"""

def addBinary(a,b):
    n = max(len(a), len(b))

    a,b = a.zfill(n), b.zfill(n)
    ans = []
    carry = 0


    for i in range(n-1, -1, -1):
        if a[i] == "1":
            carry+=1
        if b[i] == "1":
            carry+=1

        if carry % 2 ==1:
            ans.append("1")
        else:
            ans.append("0")

        carry //= 2

    if carry == 1:
        ans.append("1")
    ans.reverse()

    return ''.join(ans)


a = "11"
b = '1'

print(addBinary(a,b))