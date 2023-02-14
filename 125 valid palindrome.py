"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

"""


def validPalindrome(li):
    l = 0
    r = len(li) - 1

    while l < r:
        while l < r and not li[l].isalnum():
            l+=1
        while l < r and not li[r].isalnum():
            r-=1

        if li[l].lower() != li[r].lower():
            return False

        l+=1
        r-=1

    return True


s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))
