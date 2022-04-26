class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:  # one pass hash table O(n)
        # we use dictionary here because it has default space for value and index, and its a hash
        # table so the operations are fast
        left, right = 0, len(numbers)-1
        print(left,right)
        for i in range(len(numbers)):
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1

            elif sum > target:
                right -= 1

            else:
                return [left+1,right+1]

numbers = [-4,-2,0,1,4,5,9]
target = 2

'''numbers = [2,7,11,15]
target = 9

numbers = [-1,0]
target = -1'''
ass = Solution()
print(ass.twoSum(numbers, target))