def isValid(s):
    mapping = {'(': ')',
               '[': ']',
               '{': '}'}

    stack = []

    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        elif not stack or mapping[stack.pop()] != i:
            return False

    return not stack