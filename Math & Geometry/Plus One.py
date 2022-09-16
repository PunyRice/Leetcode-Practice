class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:  # yeah you just do it
        right = len(digits)-1
        while digits[right] == 9:
            if right > 0:
                digits[right] = 0
                right -= 1
            else:
                digits.insert(0, 1)
                digits[1] = 0
                return digits

        else:
            digits[right] += 1
            return digits

    def plusOne(self, digits: list[int]) -> list[int]:  # leet code sln
        one = 1
        i = 0
        digits = digits[::-1]

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]

    nums = []
    nums.append([1,2,3])
    nums.append([4,3,2,1])
    nums.append([9])
    nums.append([3,9,9,9,9])

    tests = nums
    print(tests)
    for i in tests:
        print("ans:",plusOne(2, i))