class Solution:
    '''def maxArea(self, height: list[int]) -> int:  # brute force
        maxAns = 0

        for i, line in enumerate(height):
            print("looking at:",i)

            for j in range(i+1,len(height)):
                #  find the area
                x, y = j-i, min(line, height[j])
                area = x*y
                print("index:", j, "countaining:",height[j], "dist:", x, "height:", y, area)

                if area > maxAns:
                    maxAns = area

            print("\n")

        return maxAns'''

    def maxArea(self, height: list[int]) -> int:  # 2 pointers
        maxAns = 0
        left, right = 0, len(height) - 1

        while left < right:
            print(left, right)

            x, y = right - left, min(height[left], height[right])
            area = x * y

            maxAns = max(maxAns, area)  # checks if this is bigger


            if height[left] < height[right]:
                left += 1

            else :
                right -= 1

        print("lol",left, right)

        return maxAns








height = [1,8,6,2,5,4,8,3,7,1,1]

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

ass = Solution()
print("final ans", ass.maxArea(height))


