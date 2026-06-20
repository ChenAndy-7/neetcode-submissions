class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{': '}', '[': ']'}
        word = []
        for i in s:
            if i in valid:
                word.append(i)
            else:
                if len(word) >= 1 and valid.get(word.pop()) == i :
                    continue
                else:
                    return False

        return True if len(word) == 0 else False
