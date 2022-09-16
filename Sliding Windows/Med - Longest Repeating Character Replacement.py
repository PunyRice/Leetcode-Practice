class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        count = {s[left]: 1}
        maxCount = 0

        while right < len(s):  # and maxCount < len(s) - (right-left+1)
            num = 0
            for v, c in count.items():
                if c > num:
                    num = c
            # num is the number of most frequently appearing char in [left, right]
            print(num, count, s[left:right+1])
            DINK = s[left:right+1]

            if (right-left+1 - num) <= k:  # checks if [left,right] is valid
                maxCount = max(maxCount, right-left+1)
                right += 1
                if s[right] in count:  # update the counter for right
                    count[s[right]] += 1
                else:
                    count[s[right]] = 1

            else:
                if s[left] in count:  # update the counter for left
                    count[s[left]] -= 1
                else:
                    count.pop(s[left])

                left += 1



            print()


        return maxCount


s = "AABABBA"
k = 1

print(dingus("asss",s,k))

    '''def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        longest = 0
        length = 0
        tempk = k

        while longest >= right:
            while s[left] != s[right] and tempk > 0:  # not the same char found

                tempk -= 1
            else:  # same char found
                length += 1
                left += 1
                right += 1
        #max(longest, right - left + 1)
        return longest'''