class Solution:
    def findMin(self, nums: list[int]) -> int:  # using binary search to remove unnecessary search space
        left, right = 0, len(nums)-1
        smallest = 9000

        while left <= right:
            mid = left + ((right-left)//2)
            # no need to check if smallest is already smallest
            if nums[mid] > smallest and nums[left] > smallest and nums[right] > smallest:
                return smallest

            if nums[left] <= nums[mid]:
                smallest = min(smallest, nums[left])
                left = mid + 1
            elif nums[right] >= nums[mid]:
                smallest = min(smallest, nums[mid])
                right = mid - 1

        return smallest
    def findMin(self, nums: list[int]) -> int:

        return



    nums = []
    nums.append([3,4,5,1,2]) # 1
    nums.append([4,5,6,7,0,1,2]) # o
    nums.append([11,13,15,17])
    nums.append([2,1])
    nums.append([1])
    nums.append([3,1,2])
    nums.append([5,1,2,3,4])
    tests = nums
    print(tests)
    for i in tests:
        print("ans:",findMin(2, i))