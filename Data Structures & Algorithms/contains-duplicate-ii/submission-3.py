class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contains = set()
        for i in range(min(k + 1, len(nums))):
            if nums[i] in contains:
                return True
            contains.add(nums[i])
        for i in range(1, len(nums) - k):
            contains.discard(nums[i - 1])
            if nums[i + k] in contains:
                return True
            contains.add(nums[i + k])
        return False