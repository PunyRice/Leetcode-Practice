class Solution:
    def countBits(self, n: int) -> list[int]: # turns int into binary, then count by for loop
        nums = list(range(n+1))
        result = []

        for i in nums:
            result.append((bin(i)[2:]).count("1"))

        return result


    def countBits1(self, n: int) -> list[int]:
        dp = [0] * (n+1)
        print(dp)
        offset = 1

        for i in range (1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp

    def countBits2(self, n: int) -> list[int]:
        # prepare the empty list for return
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            #print(i, ": ", i // 2)
            previousResult = result[i // 2]
            result[i] = previousResult + (i & 1)
        return result


    print (countBits2("ass", 10))
