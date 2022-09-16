class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:  # brute force
        result = []
        for i, v in enumerate(temperatures):  # i is left index, v is left value
            right = i+1
            while len(result) != i+1:
                if right == len(temperatures):
                    result.append(0)

                elif temperatures[right] <= v:
                    right += 1

                else:
                    result.append(right - i)


        return result

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [[temperatures[1],1]]
        result = []

        for i, v in enumerate(temperatures):
            if i < temperatures[-1][0]:  # if current is smaller than top (largest)
                result[i] = temperatures[-1][1] - i  # calculates the distance
        return

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:


    n = [73,74,75,71,69,72,76,73]
    #n = [3,2,1]
    print(dailyTemperatures("sss", n))