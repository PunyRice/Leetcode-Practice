class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        strSet = set()


        while right < len(s):

            if s[right] not in strSet:  # not repeating
                strSet.add(s[right])

                longest = max(longest, len(strSet))

            else:  # repeating
                # find last occurence of repeating char
                temps = s[0:right]  # beginning up to but not including right
                ind = right-1  # also equal to len(temps)-1
                while ind > 0:
                    if temps[ind] == s[right]:
                        break
                    else:
                        ind -= 1

                left = ind+1

            strSet = set(s[left:right + 1])  # everything between and including left and right
            right += 1

        return longest


    def lengthOfLongestSubstring(self, s: str) -> int:  #O(n)
        left = 0
        strSet = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in strSet:  # repeating char found
                strSet.remove(s[left])
                left += 1

            strSet.add(s[right])  # non repeating char
            longest = max(longest, len(strSet))  # len(strSet) = right-1
        return longest


    s = "abcxybcbb"
    #s = "umvejcuuk"

    print(lengthOfLongestSubstring("ass", s))