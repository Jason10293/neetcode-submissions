class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            sorted_list = []
            i = 0
            j = 0 

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            
            sorted_list.extend(left[i:])
            sorted_list.extend(right[j:])
            return sorted_list

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return merge(left, right)
