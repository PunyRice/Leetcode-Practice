class Solution:
    '''def isAnagram(self, s: str, t: str) -> bool:  # sorting alphebetically then compare
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t'''

    def isAnagram(self, s: str, t: str) -> bool:  # count the occurance of each letter
        if len(s) != len(t):
            return False

        countHashMap = {}

        for i in range(len(s)):
            # the get function: (key, value to return if the key doesn't exist)
            countHashMap[s[i]] = 1 + countHashMap.get(s[i], 0)
            countHashMap[t[i]] = -1 + countHashMap.get(t[i], 0)

        # at this point, if any key in countHashMap corresponds with anything but 0, it's not an anagram
        for i in countHashMap.values():
            if i != 0:
                return False

        return True





s = "ac"
t = "bb"

s = "anagram"
t = "nagaram"

ass = Solution()
print(ass.isAnagram(s,t))