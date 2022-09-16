class Solution:
    def isHappy(self, n: int) -> bool:
        # the only way the loop ends in 1 is: all digits are 0 except a single 1
        nums = str(n)
        ass = 0

        while ass < 10:  # newNum != 1:
            newNum = 0
            for num in nums:
                newNum += int(num) ** 2

            nums = str(newNum)
            print(nums)
            ass += 1

        else:
            return True

        return False

    nums = []
    nums.append(1)

    nums.append(2) # 4, 16, 37, 58, 89, 145, 42, 20, 4.....
    nums.append(3)
    nums.append(4)
    #nums.append(19)

    tests = nums
    for i in range(len(tests)):
        print(f"test {i+1} ans: {isHappy(2, tests[i])}")