class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> res = new HashSet<>();
        for (int i : nums) {
            if (res.contains(i)) {
                return true;
            } else {
            res.add(i);
            }
        }
        return false;
    }
}
