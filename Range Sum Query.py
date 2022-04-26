from itertools import accumulate

'''class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            count += self.nums[i]

        return count'''


class NumArray:  # O(n) solution using prefix sum
    def __init__(self, nums: list[int]):
        prefixSums = [0]
        curr = 0
        for i in nums:
            prefixSums.append(i+curr)
            curr += i
        print(prefixSums)
        self.prefixSums = prefixSums

    def sumRange1(self, left: int, right: int) -> int:
        return self.prefixSums[right+1] - self.prefixSums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

nums = [-2, 0, 3, -5, 2, -1]

ass = NumArray(nums)
print(ass.sumRange1(1,3))





