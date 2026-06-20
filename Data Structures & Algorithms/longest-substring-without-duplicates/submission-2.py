class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        length = set()
        longest = 0

        for fast in range(len(s)):
            while s[fast] in length:
                length.remove(s[slow])
                slow += 1

            length.add(s[fast])
            longest = max(longest, (fast - slow + 1))

        return longest



