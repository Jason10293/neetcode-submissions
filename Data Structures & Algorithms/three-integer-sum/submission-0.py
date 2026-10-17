class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -1,0,1,2,-1,-4
        -4,-1,-1,0,1,2
        """
        
        ans = []
        nums = sorted(nums) 
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            target = num * -1
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return ans
                
