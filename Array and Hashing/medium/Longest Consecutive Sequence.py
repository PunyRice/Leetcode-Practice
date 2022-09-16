class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:  # doo doo first thought, n(nlogn)
        # remove duplicates
        nums = set(nums)
        nums = list(nums)

        # sort
        nums.sort()

        longest = 0
        curr = 1
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                curr += 1
            else:
                curr = 1
            longest = max(curr, longest)
            i += 1
        print(nums)

        return longest


    def longestConsecutive(self, nums: list[int]) -> int:  # good idea
        hashset = set(nums)
        nums = list(hashset)

        longest = 0
        left, right = 1, 1

        length = 1
        while len(nums) > 0:
            while nums[0]-left in hashset:
                hashset.remove(nums[0]-left)
                nums.remove(nums[0]-left)
                left += 1
                length += 1

            while nums[0]+right in hashset:
                hashset.remove(nums[0]+right)
                nums.remove(nums[0]+right)
                right += 1
                length += 1

            longest = max(longest, length)
            hashset.remove(nums[0])
            nums.remove(nums[0])
            left, right, length = 1, 1, 1

        return longest

    def longestConsecutive(self, nums: list[int]) -> int:  # more optimized version of above
        longest = 0
        numSet = set(nums)

        for n in nums:
            # check if its the start of a sequence
            if n-1 not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
    nums = [100,4,200,1,3,2]
    #nums = [0,3,7,2,5,8,4,6,0,1]
    #nums = [0,0]
    print(longestConsecutive(2,nums))