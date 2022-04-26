class Solution:
    '''def containsDuplicate(self, nums: list[int]) -> bool:  # brute force O(n^2) time
        for i in nums:
            if nums.count(i) > 1:
                return True

        return False
    def containsDuplicate(self, nums: list[int]) -> bool: # sorting method
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False'''


    def containsDuplicate(self, nums: list[int]) -> bool:  # using a set which has no duplicates
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

nums = [1,2,3]
ass = Solution()
print(ass.containsDuplicate(nums))