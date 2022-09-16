from itertools import chain
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:  # cheese solution (flattening matrix and using prev question)
        nums = list(chain.from_iterable(matrix))
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2) # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:  # kinda gay
        width = len(matrix[0])
        left = 0
        right = width*len(matrix)-1

        while left <= right:
            mid = (right-left)//2 + left
            midInd = mid%width
            level = mid//width

            print("l,r:",left,right)
            print("mid,Ind",mid,midInd)
            print(level)
            if matrix[level][midInd] > target:
                right = mid-1

            elif matrix[level][midInd] < target:
                left = mid+1
            else:
                return True

        return False




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  # neetcode soln, finding row, then using binary serach
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 64

    print("ans:",searchMatrix(2, matrix, target))

