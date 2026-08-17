class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, st = list(s), list(t)
        ss.sort(), st.sort()

        if ss == st:
            return True

        else:
            return False