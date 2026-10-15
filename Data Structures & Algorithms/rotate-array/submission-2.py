class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        slice = len(nums) - k
        nums += (nums[:slice])
        del nums[:slice]

        
        
        