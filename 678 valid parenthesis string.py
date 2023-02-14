"""

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true

"""

class Solution:
    def checkValidString(self, s: str) -> bool:

        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0


        """
        When you met "(", you know you need one only one ")", cmin = 1 and cmax = 1.
        When you met "(*(", you know you need one/two/three ")", cmin = 1 and cmax = 3.

        The string is valid for 2 condition:

        cmax will never be negative.
        cmin is 0 at the end.


        cmax counts the maximum open parenthesis,
        which means the maximum number of unbalanced '(' that COULD be paired.
        cmin counts the minimum open parenthesis,
        which means the number of unbalanced '(' that MUST be paired.

        """