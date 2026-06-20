class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        tracker = []
        for i in strs:
            tracker.append(i)
        
        while len(tracker) != 0:
            torm = []
            simWords = []
            i = 0
            a = ""
            for word in tracker:
                if i == 0:
                    a = "".join(sorted(word))
                    simWords.append(word)
                    i += 1
                    torm.append(word)
                elif a == "".join(sorted(word)):
                    simWords.append(word)
                    torm.append(word)
            for w in torm:
                tracker.remove(w)
            ans.append(simWords)
        return ans