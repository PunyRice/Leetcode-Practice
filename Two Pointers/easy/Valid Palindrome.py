class Solution:
    '''def isPalindrome(self, s: str) -> bool:  # flip string and compare
        s = s.lower()  # convert to lower case
        reverseStr = ""
        for i in range(len(s)-1, -1, -1):  # (start, stop, interval)
            # 97-122 are ascii letter range, 48-57 are ascii number range (inclusive)
            if 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57:
                reverseStr += s[i]
                if reverseStr
            else:  # non alphanumeric character
                s = s.replace(s[i], "", 1)  # the 1 is how many instances to remove

        return reverseStr == s'''

    def isPalindrome(self, s: str) -> bool:  # flip string and compare
        s = s.lower()  # convert to lower case and remove all spaces

        while not s:
            # 97-122 are ascii letter range, 48-57 are ascii number range (inclusive)
            print(i)
            if not(97 <= ord(s[i]) <= 122) and not(48 <= ord(s[i]) <= 57):
                s = s.replace(s[i], "")

        for i in range(len(s)-1):
            print(s[i], s[len(s)-1-i])
            if s[i] != s[-(i+1)]:
                return False


        return True

s = "rac,ecar"
s = "A man, a plan, a canal: Panama"
ass = Solution()
print(ass.isPalindrome(s))
