"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

"""

class Solution:
    def countAndSay(self, n: int) -> str:

        seq = '1'
        for i in range(n-1):
            seq = self.getNext(seq)
        return seq


    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            while i < len(seq)-1 and seq[i] == seq[i+1]:
                count +=1
                i += 1
            next_seq+=str(count)+seq[i]
            i+=1

        return next_seq