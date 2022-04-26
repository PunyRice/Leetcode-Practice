class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        # solution 1, retard intuitive way, find each unique element, count everything this so fucking slow jesus 3500ms
        result = set()
        for i in nums:
            result.add(i)

        result = list(result)
        for i in result:
            if nums.count(i) != 2:
                return i

    def singleNumber1(self, nums: list[int]) -> int:
        # solution 2, using xor gates, cancel everything except the single number
        result = 0
        for i in nums:
            # Find XOR with the result
            result ^= i
        return result

    def singleNumber2(self, nums: list[int]) -> int:
        # solution 3, using maths, get set of nums
        '''noDup = set(nums)+
        return -(sum(nums) - 2*sum(noDup))'''
        
        return 2*sum(set(nums)) - sum(nums)





    def singleNumber3(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) != 2:
                return i

















    nums = [1] #[1,2,3,2,3,5,5]
    print(singleNumber3("ass", nums))









