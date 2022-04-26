class Solution:
    def climbStairs(self, n: int) -> int:
        stepCount = 1
        preStepCount = 1
        result = 0

        for i in range(n):
            result = stepCount + preStepCount
            stepCount = preStepCount
            preStepCount = result
            print(result)
        return result

    def climbStairs1(self, n: int) -> int: # this is basically finding fibonatchi numbers for n
        # set up the array
        first, second = 1, 1

        for i in range(n-1):
            temp = first
            first += second
            second = temp
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a
            """"""
        return first

    print(climbStairs1("ass", 1))