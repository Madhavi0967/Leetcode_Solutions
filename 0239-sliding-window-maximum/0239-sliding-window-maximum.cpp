class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            if (!dq.empty() &&
                dq.front() == i - k) // to remove elements that are outside
                dq.pop_front();

            while (!dq.empty() &&
                nums[dq.back()] < nums[i]) // remove smallest element
                dq.pop_back();

            dq.push_back(i); // adding present one

            if (i >= k - 1)
                ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};