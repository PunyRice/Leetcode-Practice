class Solution:
    def trap(self, height: list[int]) -> int:  #O(n) memory solution
        # find the maxleft and maxright water level for each index
        # then take the min(maxleft at i, maxright at i) - waterlevel at i, that is the amount of water trapped

        # this implimentation can be slightly sped up by recording where the max is, and skipping calculations from i
        # up to that max location (checking for rightMax). a similar thing can be done for leftMax


        leftMax, rightMax = height[0], 0
        water = 0

        for i in range(len(height)):
            # height[0: i] is 0 to i (not including i)
            leftMax = max(height[0: i], default=0)  # if the list is empty, return 0

            # height[i: len(height)] is i to the end of the list (not including i)
            rightMax = max(height[i+1: len(height)], default=0)  # if the list is empty, return 0

            possibleWater = min(leftMax,rightMax)-height[i]
            if possibleWater > 0:
                water += possibleWater


            print(leftMax, rightMax)

        return water

    def trap(self, height: list[int]) -> int:  #O(1) memory solution, two pointers
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        water = 0

        for z in range(len(height)):
            if leftMax < rightMax:  # deciding to shift left or right pointer
                if leftMax - height[left] > 0:  # checking if water is negative
                    water += leftMax - height[left]

                left += 1  # shift the smaller pointer


            else:  #leftMax >= rightMax
                if rightMax - height[right] > 0:  # checking if water is negative
                    water += rightMax - height[right]

                right -= 1  # shift the smaller pointer

            rightMax = max(height[right], rightMax)  # update the max value using current index
            leftMax = max(height[left], leftMax)  # update the max value using current index

        return water




height = [0,1,0,2,1,0,1,3,2,1,2,1]


ass = Solution()
print("final ans", ass.trap(height))