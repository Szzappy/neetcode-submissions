public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, List<int>> ints = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Length; i ++){
            if (!ints.ContainsKey(nums[i]))
                ints[nums[i]] = new List<int>();
            ints[nums[i]].Add(i);
        }

        for (int i = 0; i < nums.Length; i ++){
            if (ints.ContainsKey(target - nums[i])){
                if (ints[target - nums[i]].Count == 2)
                    return new int[] {i, ints[target - nums[i]][1]};
                else if (target - nums[i] != nums[i])
                    return new int[] {i, ints[target - nums[i]][0]};
            }
        }

        return null;
    }
}
