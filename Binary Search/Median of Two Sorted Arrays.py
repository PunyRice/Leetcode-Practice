class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:  # brute force merge
        nums1.extend(nums2)
        nums1.sort()

        left, right = 0, len(nums1)-1
        mid = divmod(left+(right-left), 2)
        print(mid)
        print(nums1)
        if mid[1] == 0:
            return nums1[mid[0]]

        else:
            return (nums1[mid[0]] + nums1[mid[0]+1]) / 2

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # merge nums1 into nums2, binary search is used on num2
        merged = nums2[0:len(nums2)]  # merged has nums2, nums1 will be added into merged

        for target in nums1:
            left, right = 0, len(merged)-1

            while left <= right:
                mid = left+((right-left) // 2)
                print(left, mid, right)

                # check out of bounds
                if merged[right] <= target:
                    merged.insert(right+1, target)
                    break
                elif merged[left] >= target:
                    merged.insert(left, target)
                    break

                # binary search
                if merged[mid] > target:
                    right = mid - 1
                elif merged[mid] < target:
                    left = mid + 1
                else:
                    print(f"equallllllllll, {left},{right}")  # same value found
                    merged.insert(mid,target)
                    break
        print("Array with added value", merged, nums1)
        print(len(merged)+len(nums1))
        # find median
        if merged == []:
            merged = nums1

        if len(merged)+len(nums1) == 0:
            return 0.0


        # find median
        mid = divmod(len(merged)-1, 2)
        print(mid)
        print(merged)
        if mid[1] == 0:
            return merged[mid[0]]
        else:
            return (merged[mid[0]] + merged[mid[0]+mid[1]]) / 2

    nums = []
    '''nums.append([[1,5,6],[2,3,4,9,10]])  # 1 2 3 4 5 6 9 10
    nums.append([[1,4,10],[2,9,40,90]])  # 1 2 4 9 10 40 90
    nums.append([[10],[1,4,6,10]])  # 1,4,6,10,10
    nums.append([[10],[10]])'''

    #nums.append([[], [2]])
    #nums.append([[2], []])
    nums.append([[], []])
    tests = nums
    for nums1, nums2 in tests:
        print("ans:",findMedianSortedArrays(2, nums1, nums2))