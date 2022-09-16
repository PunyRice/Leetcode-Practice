class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        # these have 1 less element than nums, these are the prefix products
        leftSide = [nums[0]]  # has the first element
        rightSide = [nums[len(nums)-1]]  # has the last element

        for i in range(1,len(nums),1):
            leftSide.append(leftSide[i-1]*nums[i])
        nums.reverse()
        for i in range(1,len(nums),1):
            rightSide.append(rightSide[i-1]*nums[i])

        leftSide.insert(0,1)
        rightSide.reverse()
        rightSide.insert(len(nums),1)

        print(leftSide, rightSide)

        # multiply parts of the prefix product to find ans
        for i in range(len(nums)):
            ans.append(leftSide[i]*rightSide[i+1])

        return ans

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1  # leftside
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1  # rightside5
        for i in range(len(nums)-1, -1, -1):  # start from end, end at first element, decrement by -1
            res[i] *= postfix  # combine left and right
            postfix *= nums[i]

        return res

    nums = [-1,1,0,-3,3]
    print(productExceptSelf(2,nums))

