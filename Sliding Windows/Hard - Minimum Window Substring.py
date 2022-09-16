import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:  # s is bigger, t is the target to be found
        left,right = 0,1
        tMap = collections.defaultdict(int)  # key: string, value, count
        windowMap = collections.defaultdict(int)
        minLength = (0,1000000000000000000)

        for char in t:
            tMap[char] += 1

        for char in s[left:right]:
            if char in tMap:  # only count the target chars
                windowMap[char] += 1

        while right < len(s)-1:
            while windowMap != tMap:  # if the windows dont match
                print(windowMap.items(), "dont match", left,right)
                # s[right] is the char in string at right position

                if s[right] in tMap and windowMap[s[right]] < tMap[s[right]]:  # needs to be a target and needs to be correct amount of target
                    windowMap[s[right]] += 1

                if windowMap != tMap:  # after the prev if, condition might be furfilled
                    right += 1
            else:  # if the windows do match
                if right-left < minLength[1]-minLength[0]:  # compare, minLength[1] is right, minLength[0] is left
                    minLength = (left, right)

                windowMap[s[left]] -= 1  # do this so windows don't match anymore
                left += 1
                while s[left] not in tMap:  # move left to next matching location
                    left += 1

                print(windowMap.items(), "match, new thing:", left,right)

        print(windowMap, left, right)



        return minLength







    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""



    s = "ADOBECODEBANC"
    t = "ABC"

    '''s = "a"
    t = "a"
    
    s = "a"
    t = "aa"'''

    print(minWindow("asss",s,t))