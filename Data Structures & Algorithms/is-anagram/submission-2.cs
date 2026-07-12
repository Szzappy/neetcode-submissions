public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;
        int s_size = s.Length;
        Dictionary<char, List<int>> s_table = new Dictionary<char, List<int>>();
        for (int i = 0; i < s.Length; i ++){
            if (!s_table.ContainsKey(s[i]))
                s_table[s[i]] = new List<int>();

            s_table[s[i]].Add(i);
        }

        foreach (char c in t) {
            if (s_table.ContainsKey(c) && s_table[c].Count > 0) {
                s_table[c].RemoveAt(0);
                s_size -= 1;
            }
        }

        if (s_size == 0) {
            return true;
        }

        return false;
    }
}
