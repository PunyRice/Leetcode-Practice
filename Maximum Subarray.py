def maxSubarray(nums: list[int]) -> int:  # O(n^2) solution
    biggest = max(nums)
    ans = []

    for i in range(len(nums)):
        curr = nums[0]
        for j in range(1, len(nums)):
            curr += nums[j]
            ans.append(curr)
        nums.pop(0)

    ans.append(biggest)
    return max(ans)



def maxSubarray2(nums: list[int]) -> int:  # O(n) solution
    maxSub = nums[0]
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSub = max(maxSub, currSum)
    return maxSub












nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [-1,4,-2,-3,5]

#print(maxSubarray(nums))
print(maxSubarray2(nums))

