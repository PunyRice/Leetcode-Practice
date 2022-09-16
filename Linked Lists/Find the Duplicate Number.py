class Solution:
    def findDuplicate(self, nums: [int]) -> int:  # shiddy hashmap sln
        hashMap = set()
        for i in nums:
            if i in hashMap:
                return i
            hashMap.add(i)

    def findDuplicate(self, nums: [int]) -> int:  # floyds cycle detction
        slow, fast = 0, 0

        # find the place fast and slow intesect
        while True:  # we set true because we know that slow and fast must intercept when theres a loop, which this question gaureentees
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # phase 2, move 2 slow pointers until they meet
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


