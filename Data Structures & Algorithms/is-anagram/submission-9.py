class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = defaultdict(int)

        if len(s) != len(t):
            return False

            
        for i in s:
            hmap[i] += 1

        for j in t:
            hmap[j] -= 1
            if hmap[j] < 0:
                return False

        return True