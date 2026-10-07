class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        sum = 0
        left = 0
        for right, value in enumerate(nums):
            sum += value
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        
        return 0 if ans == float('inf') else ans