class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        for c in s:
            seen[c] += 1

        for x in t:
            if x in seen:
                seen[x] -= 1
                if seen[x] < 0:
                    return False
            else:
                return False

        for y in seen:
            if seen[y] != 0:
                return False

        return True