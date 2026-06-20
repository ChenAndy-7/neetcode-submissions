class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c)- 97] += 1
            output[tuple(arr)].append(s)

        return list(output.values())

