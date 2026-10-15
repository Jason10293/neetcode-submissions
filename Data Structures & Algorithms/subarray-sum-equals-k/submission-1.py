class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = {0: 1}
        currSum = 0

        for num in nums:
            currSum += num
            target = currSum - k
            res += count.get(target, 0)

            count[currSum] = count.get(currSum, 0) + 1
        return res