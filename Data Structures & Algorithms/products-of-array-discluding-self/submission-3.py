class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        brute force:
        loop through every number skipping one element each time
        O(n^2)

        how can I keep track of repeated products?
        48,24,12,8 
        2 * 4 * 6
        1 * 4 * 6
        1 * 2 * 6
        1 * 2 * 4

        [1, 1, 2, 8]
        [1, 6, 24, 48]

        
        
        """
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        ans = [0] * n

        pre[0] = suf[n - 1] = 1
        for i in range(1,n):
            pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]
        
        for i in range(n):
            ans[i] = pre[i] * suf[i]

        return ans