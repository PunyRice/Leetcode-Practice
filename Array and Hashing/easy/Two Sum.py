class Solution:
    '''def twoSum(self, nums: list[int], target: int) -> list[int]:  # retard solution O(n^2)
        length = range(len(nums))
        for i in length:
            for j in length:
                if nums[i]+nums[j] == target and i != j:
                    return [i, j]'''

    def twoSum(self, nums: list[int], target: int) -> list[int]:  # one pass hash table O(n)
        # we use dictionary here because it has default space for value and index, and its a hash
        # table so the operations are fast
        numsDict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            # if the difference is in nums, that difference must be the other number
            if difference in numsDict:
                return [numsDict[difference],i]

            # add the item to the hash table
            numsDict[nums[i]] = i

nums = [11,2,7,15,16]
target = 9

nums = [3,3]
target = 6

ass = Solution()
print(ass.twoSum(nums, target))