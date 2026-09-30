class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Idea: use two pointers 
        L -> first element
        R -> last element
        while loop
        if L or R elem == 2
        k += 1
        move right pointer until element != 2
        move left point until element == 2
        swap elem at L and R pointers
        loop
        """

        # if len(nums) == 1 and nums[0] == val:
        #     nums = []
        #     return 0
        left = 0
        right = len(nums) - 1
        k = len(nums)

        while left <= right:
            while left <= right and nums[right] == val:
                k -= 1
                right  -= 1

            while left <= right and nums[left] != val:
                left += 1

            if left <= right:
                k -= 1
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return k



