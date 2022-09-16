class Solution:
    # general idea solution
    def evalRPN(self, tokens: list[str]) -> int:
        operator = ""
        numStack = []

        for i in tokens:
            if i in "+-*/":  # if the token is an operation
                print("eeeeeeeeeeeeeeeee", numStack)

                if i == "+": num = numStack[-2] + numStack[-1]
                if i == "-": num = numStack[-2] - numStack[-1]
                if i == "*": num = numStack[-2] * numStack[-1]
                if i == "/": num = int(numStack[-2] / numStack[-1])  # the int() rounds decimals to int
                numStack.pop()
                numStack.pop()
                numStack.append(num)
            else:  # if the token is a number
                numStack.append(int(i))

        return numStack[0]
 
    # less clean faster solution
    def evalRPN(self, tokens: list[str]) -> int:
        operator = ""
        numStack = []

        for i in tokens:

            if i == "+":
                num = numStack[-2] + numStack[-1]
                numStack.pop()
                numStack.pop()
                numStack.append(num)
            elif i == "-":
                num = numStack[-2] - numStack[-1]
                numStack.pop()
                numStack.pop()
                numStack.append(num)
            elif i == "*":
                num = numStack[-2] * numStack[-1]
                numStack.pop()
                numStack.pop()
                numStack.append(num)
            elif i == "/":
                num = int(numStack[-2] / numStack[-1])  # the int() rounds decimals to int
                numStack.pop()
                numStack.pop()
                numStack.append(num)

            else:  # if the token is a number
                numStack.append(int(i))

        return numStack[0]
    print(evalRPN("ass", ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))