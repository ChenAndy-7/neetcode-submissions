class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> tracker = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (tracker.contains(nums[i])) {
                return true;
            } else {
                tracker.add(nums[i]);
            }
        }
        return false;
    }
}
