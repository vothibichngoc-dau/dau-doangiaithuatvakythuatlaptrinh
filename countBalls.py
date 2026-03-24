class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        unordered_map<int, int> boxCount;
        int maxBalls = 0;
        
        for (int i = lowLimit; i <= highLimit; i++) {
            int sum = 0, n = i;
            while (n > 0) {
                sum += n % 10;
                n /= 10;
            }
            
            boxCount[sum]++;
            maxBalls = max(maxBalls, boxCount[sum]);
        }
        
        return maxBalls;
    }
};