class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        1,2,4,5
        1,2,2,3,3
        """
        people = sorted(people)
        left = 0
        right = len(people) - 1
        ans = 0
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            ans += 1
        return ans + 1 if (right == left) else ans
                
                