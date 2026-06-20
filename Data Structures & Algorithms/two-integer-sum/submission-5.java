class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int difference;
            difference = target - nums[i];

            if (map.get(difference) != null) {
                int val = map.get(difference);
                if (i != val) {
               return new int[] {i, val};
            }
            }
        }
        return new int[]{};

    }
}
