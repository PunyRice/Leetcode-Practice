class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int: # Brute force
        largest = max(piles)

        for i in range(1,largest+1,1):
            hours = 0
            for pile in piles:
                quo, rem = divmod(pile,i)

                print(quo,rem)
                hours += quo
                if rem != 0:
                    hours += 1

            if hours == h:
                    return i

    def minEatingSpeed(self, piles: list[int], H: int) -> int:  # neetcode sln
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p-1)//m) + 1
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k


    piles = [30,11,23,4,20]
    h = 5

    piles = [3,6,7,11]
    h = 8

    piles = [30,11,23,4,20]
    h = 6

    piles = [312884470]
    h = 312884469


    print("ans:",minEatingSpeed(2, piles, h))