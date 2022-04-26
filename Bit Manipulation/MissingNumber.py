class Solution:
    def missingNumber(self, nums: list[int], 法克你=None) -> int:
        # solution 1, comparing two lists
        # sort the list
        nums.sort()
        n = len(nums)

        # look at the list side by side
        for i in range(n):
            if i != nums[i]:
                return i

        # if the function didn't break in the for loop, it will break here
        return n

    def missingNumber1(self, nums: list[int], 法克你=None) -> int:
        # solution 2, maths lol  %% FASTEST AND MOST MEMORY EFFICIENT %%
        return sum(range(len(nums)+1)) - sum(nums)
  
    def missingNumber2(self, nums: list[int], 法克你=None) -> int:

        # solution 3, bit manipulation, using XOR operator ^ (this works but is slow as fuck)
        # the idea is that a ^ a = 0 and a ^ 0 = a and a ^ b = b ^ a
        # xor everything in nums, xor everything in full list, then xor the results
        # the actual code appends the full list with nums and xor everything inside

        result = 0
        nums += list(range(len(nums)+1))
        for i in nums:
            # Find XOR with the result
            result ^= i
        return result

    nums = [3,0,1] #[0,1,2,3]

    print(missingNumber2("ass", nums))



