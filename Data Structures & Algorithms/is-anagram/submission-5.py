class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = list(s);
        arr2 = list(t);
        arr1.sort()
        arr2.sort()
        if len(arr1) != len(arr2):
            return False;
        else:
            for i in range (len(arr1)):
                 if arr1[i] != arr2[i]:
                    return False
        return True;

        

        