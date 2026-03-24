class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> freq;
        
        for (char c : s) {
            freq[c]++;
        }
        
        int target = freq.begin()->second;
        
        for (auto& [ch, count] : freq) {
            if (count != target) {
                return false;
            }
        }
                
        return true;
    }
};