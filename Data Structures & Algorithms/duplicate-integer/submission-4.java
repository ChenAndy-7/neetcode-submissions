// import java.util.HashSet;

class Solution {
    public boolean hasDuplicate(int[] nums) {
    HashSet <Integer> allNum = new HashSet<Integer>();
    for (int i = 0; i < nums.length; i++) {
        if (!allNum.contains(nums[i])) {
            allNum.add(nums[i]);
        } else {
            return true;
        }
    }
    return false;
    }
    
}
