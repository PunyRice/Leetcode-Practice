import random
randomlist = []
for i in range(0,20):
    n = random.randint(1,50)
    randomlist.append(n)
print(randomlist)


'''class Solution:
    def trap(self, height: list[int]) -> int:
        rainWater = 0
        tempWater = 0
        left, right = 0, 1

        while left < right:
            print(left, right)

            if height[left] <= height[right]:
                left += 1
                right += 1
                if tempWater != 0:


            elif height[left] > height[right]:
                tempWater += height[left] - height[right]
                right += 1

            left, right = right, right + 1

        print("lol", left, right)

        return rainWater


height = [0, 1, 0, 2, 1, 0, 1, 3]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]

ass = Solution()
print("final ans", ass.trap(height))'''


height = [0,1,0,2,1,0,1,3]
#height = [0,1,0,2,1,0,1,3,2,1,2,1]

ass = Solution()
print("final ans", ass.trap(height))

