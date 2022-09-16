class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}  # in the format of count : number
        occurances = [[] for i in range(len(nums)+1)]


        for n in nums:
            counter[n] = 1 + counter.get(n,0)  # returns nothing if i doesn't exist in counter

        for n, c in counter.items():  # n is the number, c is count
            occurances[c].append(n)  # at index 0 is the least occuring number

        ans = []
        for i in range(len(occurances)-1, 0, -1):  # i will count down from the last occurance to the first
            for n in occurances[i]:  # another for loop needed for the 2d array
                ans.append(n)
            if len(ans) == k:
                return ans

        print(occurances)
        print(counter)
        print(ans)


    nums = [1]

    k = 1
    print(topKFrequent(23, nums, k))
