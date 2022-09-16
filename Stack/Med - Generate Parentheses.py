class Solution:
    def generateParenthesis(self, n: int) -> list[str]:  # neet code soln
        # only add open paranthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IFF open == closed == n
        stack = []
        res = []

        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:  # adding open pareanthes
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:  # adding open pareanthes
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
    n = 3
    print(generateParenthesis("sss", n))

