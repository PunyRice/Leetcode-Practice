class Solution:
    '''def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        checked = "b"  # check for duplicate numbers so we dont have to calc again
        ansLib = set()


        for index, num in enumerate(nums):
            temp = (nums[0: index] + nums[index + 1: len(nums)])


            target = -(num)

            print("looking at:",num, temp, checked)

            # check inner
            left, right = 0, len(temp) - 1
            while num != checked and left < right :
                sum = temp[left] + temp[right]
                print(sum)
                if sum < target:
                    left += 1

                elif sum > target:
                    right -= 1

                else:  # answer found
                    tempAns = [num, temp[left], temp[right]]
                    tempAns.sort()  # sort the answer so its smallest to biggest

                    left += 1
                    right -= 1
                    if tuple(tempAns) not in ansLib:
                        ansLib.add(tuple(tempAns))


            checked = num


            print("ans",  ansLib, "\n")

        return list(ansLib)'''

    def threeSum(self, nums: list[int]) -> list[list[int]]:  # no need to save duplicates
        nums.sort()
        ans = []

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:  # check for duplicate numbers so we dont have to calc again
                continue

            # check inner
            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1

                elif threeSum > 0:
                    right -= 1

                else:  # answer found
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1


            print("ans", ans, "\n")

        return ans


nums = [-1, -1, 0, 1, 2, 4]
#nums = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]

#nums = [-7, -2, -2, -1, -1, 0, 1, 2, 4, 8]
#nums = [-1,0,1,0]
ass = Solution()
print("final ans", ass.threeSum(nums))
