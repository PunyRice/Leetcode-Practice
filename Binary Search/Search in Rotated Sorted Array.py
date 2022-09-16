class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = ((r - l) // 2) + l

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:  # m is in left portion
                if nums[m] < target:
                    l = m + 1
                else:
                    if nums[l] <= target: # would mean that l < target < m
                        r = m - 1
                    else:
                        l = m + 1
            else:  # m ins in right portion l > m
                if nums[m] > target:
                    r = m - 1
                else:
                    if nums[r] <= target: # would mean that m < target < r
                        r = m - 1
                    else:
                        l = m + 1


        return -1


    def search(self, nums: list[int], target: int) -> int:  # neetcode soln
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:  # m is in left portion
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:  # m ins in right portion l > m
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return -1

    nums = [4,5,6,7,0,1,2]
    target = 0  # ANS = 4

    nums = [4,5,6,7,0,1,2]
    target = 3  # ANS -1

    nums = [1]
    target = 0  # ANS -1

    nums = [5,1,3]
    target = 5
    print("ans:",search(2,nums,target))