public class Solution {
    public bool hasDuplicate(int[] nums) {
         Dictionary<int, int> hashTable = new Dictionary<int, int>();

         for (int i = 0; i < nums.Length; i ++) {
            if (hashTable.ContainsKey(nums[i]))
                return true;
            hashTable[nums[i]] = i;
         }
         return false;
    }
}