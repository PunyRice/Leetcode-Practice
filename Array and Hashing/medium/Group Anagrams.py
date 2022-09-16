from collections import defaultdict  # needed for groupAnagrams1
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # dictionary = {sorted string: ["anagram1", "anagram2"]}
        dictionary = {''.join(sorted(strs[0])): [strs[0]]}

        strs.remove(strs[0])  # removes the first word
        print(strs)
        for i in strs:
            sort = ''.join(sorted(i))  # sort the current word
            print(i,sort)
            if sort in dictionary:
                thing = dictionary[sort]
                thing.append(i)  # add new instance under the existing anagram

            else:
                dictionary[sort] = [i]  # add completely new catagory
        print(dictionary)

        return list(dictionary.values())


    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:  # using lots of other functions
        result = defaultdict(list)  # Defining a dictionary with values as a list

        for i in strs:
            count = [0] * 26  # a to z

            for char in i:
                count[ord(char) - ord("a")] += 1

            # at this point count is a list of length 26 where each letter is counted

            result[tuple(count)].append(i)

        return result.values
    strs = ["eat","tea","tan","ate","nat","bat"]

    print(groupAnagrams1(23, strs))