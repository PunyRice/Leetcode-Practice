class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return 0




    def maxProfit1(self, prices: list[int]) -> int:
        l,r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]- prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1

        return maxP

    prices = [1,2,9999,0,1]
    print(maxProfit("ass", prices))









