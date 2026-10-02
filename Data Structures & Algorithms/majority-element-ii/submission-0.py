from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        total_elems = len(nums)

        map = defaultdict(int)

        for num in nums:
            map[num] += 1
        
        ans = []
        for index, (key, values) in enumerate(map.items()):
            if values > total_elems // 3:
                ans.append(key)

        
        return ans