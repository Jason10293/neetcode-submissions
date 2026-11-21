class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            if index == len(nums):
                ans.append(path[:])
                return


            # Choice 1: choose to take the number
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # Choice 2: not choose to take the number
            backtrack(index + 1, path)

        backtrack(0, [])

        return ans