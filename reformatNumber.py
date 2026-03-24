class Solution {
public:
    string reformatNumber(string number) {
        string digits = "";
        for (char c : number) {
            if (isdigit(c)) digits += c;
        }
        
        string res = "";
        int i = 0;
        int n = digits.size();
        while (n - i > 4) {
            res += digits.substr(i, 3) + "-";
            i += 3;
        }
        int remaining = n - i;
        if (remaining == 4) {
            res += digits.substr(i, 2) + "-" + digits.substr(i + 2, 2);
        } else {
            res += digits.substr(i, remaining);
        }
        
        return res;
    }
};