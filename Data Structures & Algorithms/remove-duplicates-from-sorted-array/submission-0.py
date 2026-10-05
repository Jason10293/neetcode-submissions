class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        have two pointers
        one stays at the first instance of a num
        second one moves until a new num is found --> k += 1
        first + 1 = new num
        first = second

        """
        slow = 1  # next write position; nums[0] is always unique

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
            

            
        return k