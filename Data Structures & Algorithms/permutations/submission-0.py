class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            
            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False


        backtrack([])
        return ans