class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            j = i + 1
            for j in range(j, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    print(j ,"-", i)
                    res[i] = j - i
                    break
            
        return res


