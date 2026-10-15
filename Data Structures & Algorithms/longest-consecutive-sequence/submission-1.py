class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        seen = {}
        for num in nums:
            numSet.add(num)
        
        ans = 0
        for index, num in enumerate(nums):
            curr = num
            counter = 0
            if curr + 1 in numSet:
                continue
            while curr in numSet:
                counter += 1
                curr -= 1
            ans = max(ans, counter)
        return ans

