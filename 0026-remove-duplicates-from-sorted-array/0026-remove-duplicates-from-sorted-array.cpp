class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        int k = 1;  // Pointer for the next unique position
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];
                ++k;
            }
        }
        return k;

    }
};