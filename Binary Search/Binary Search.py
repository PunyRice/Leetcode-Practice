class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = ((right-left)//2) + left
            print(mid,left,right)
            if target < nums[mid]:  # target is leftside of mid
                right = mid-1
            elif target > nums[mid]:  # target is rightside of mid
                left = mid+1
            else:
                return mid
        return -1

    def search(self, nums: list[int], target: int) -> int:  # neet code solution
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2) # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

    nums = [1]
    target = 1
    #nums = [-1,0,3,5,9,12]
    #target = 2
    print("ans:",search(2,nums,target))