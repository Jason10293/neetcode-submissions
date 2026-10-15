class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        2, -1, 1, 2
        0, 2, 1, 2, 4

        prefix[j + 1] - prefix[i] = k
        prefix[i] = prefix[j + 1] - k

        create prefix sum array 
        scan left to right through the array
        calculate current position - prefix_sum = n
        n exists? 
        if not: add curr_position to hashmap
        does exist: count of all positions where curr_pos - prefix_sum = n
        """
        count = {0: 1}
        running_sum = 0
        ans = 0

        for num in nums:
            running_sum += num
            ans += count.get(running_sum - k, 0)
            count[running_sum] = count.get(running_sum, 0) + 1

        return ans
