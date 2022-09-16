class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # neetcode solution
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res


    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0, 1
        maxProfit = 0

        while r < len(prices):

            if prices[l] > prices[r]:  # purchase cannot be made
                l = r
                r += 1
            else:
                profit = prices[r]-prices[l]
                maxProfit = max(profit,maxProfit)
                r += 1

        return maxProfit

    prices = [7,1,5,3,6,4]
    prices =[2,1,2,1,0,1,2]
    print(maxProfit("ass", prices))









