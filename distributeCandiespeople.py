class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> res(num_people, 0);
        int i = 0;
        int give = 1;
        
        while (candies > 0) {
            int curr = min(give, candies);
            res[i] += curr;
            candies -= curr;
            
            give++;
            i = (i + 1) % num_people;
        }
        
        return res;
    }
};