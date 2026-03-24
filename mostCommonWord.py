class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> ban(banned.begin(), banned.end());
        unordered_map<string, int> freq;
        
        for (char &c : paragraph) {
            if (!isalpha(c)) c = ' ';
            else c = tolower(c);
        }
        
        string word;
        stringstream ss(paragraph);
        string res;
        int maxCount = 0;
        
        while (ss >> word) {
            if (ban.find(word) == ban.end()) {
                freq[word]++;
                
                if (freq[word] > maxCount) {
                    maxCount = freq[word];
                    res = word;
                }
            }
        }
        
        return res;
    }
};