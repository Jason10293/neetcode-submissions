class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        def backtrack(index, path):
            if index == len(nums):
                ans.append(path[:])
                return
                
            path.append(nums[index])
            backtrack(index + 1, path)
            
            popped = path.pop()
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == popped:
                next_index += 1 

            backtrack(next_index, path)


        backtrack(0, [])
        return ans