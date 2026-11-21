class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ans = []
        seen = set()
        nums = sorted(nums)
        def backtrack(start, remaining, path):
            if remaining == 0:
                ans.append(path[:])
                return
            
            for i in range(start, len(nums)):
                num = nums[i]
                if num > remaining:
                    break
                
                path.append(num)
                backtrack(i, remaining - num, path)
                path.pop()
            
        backtrack(0, target, [])
        return ans

            