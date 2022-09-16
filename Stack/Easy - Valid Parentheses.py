class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # left is bottom, right is top, aka stack[-1]
        brackets = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        if len(s)%2 != 0:  # if there are odd number of brackets in s
            return False

        for i in s:
            if i in ")]}":  # if its ending bracket
                if not bool(stack) or stack[-1] != brackets[i]:  # if the stack is empty or if the brackets dont match
                    return False

                else:
                    stack.pop()
            else:
                stack.append(i)

        return not bool(stack)  # bool(stack) is false if stack is empty


    s = "()[]{}"
    s = "{[)]}"
    s = "){"
    print(isValid("ass", s))