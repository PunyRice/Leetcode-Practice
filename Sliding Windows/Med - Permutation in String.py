import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  # sliding windows with dict
        l, r = 0, len(s1)

        # put s1 into hashmap
        s1HashMap = collections.defaultdict(int)
        for i in s1:
            s1HashMap[i] += 1

        s2HashMap = collections.defaultdict(int)


        while r < len(s2)+1:
            for i in s2[l:r]:  # put the len(s1) sized window of s2 into s2hashmap
                s2HashMap[i] += 1
            print(s2[l:r])
            print(s2HashMap)
            if s2HashMap == s1HashMap:  # if s1hashmap is equal to s2hashmap then a match is found
                return True
            l+=1  # update the window
            r+=1
            s2HashMap.clear()

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:  # neetcode soln taking advantage of the fact that only 26 possible s1 and s2 combos
        if len(s1) > len(s2): return False  # cant be found if s1 is bigger
        s1Count, s2Count = [0] * 26, [0] * 26  # index is alphabet # (aka letter), and value at index is count
        print(s1Count)
        # initialize both arrays
        for i in range(len(s1)):  # a is 97, z is 122 in ascii
            print(s2[i])
            s1Count[ord(s1[i])-97] += 1
            s2Count[ord(s2[i])-97] += 1

        matches = 0
        for i in range(26):  # compare both arrays
            matches += (1 if s1Count[i] == s2Count[i] else 0)  # increment matches if equal, if not, dont do anything

        l = 0
        for r in range(len(s1), len(s2)):  # start r at next s2Count window
            if matches == 26: return True  # if both arrays are equal return true

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26



    s1 = "ab"
    s2 = "eidbaooo"
    #s2 = "eidboaoo"

    s1 = "hello"
    s2 = "ooolleoooleh"


    print(checkInclusion("asss",s1,s2))