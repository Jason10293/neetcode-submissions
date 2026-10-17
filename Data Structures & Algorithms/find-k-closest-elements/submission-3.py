class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Keep a window of size k
        keep track of the max distance from the target
        will the element always be consecutive? --> yes
        what makes one window better than another?
            dont need to keep track of the middle elements
            we'll compare windows based on the max(arr[0], arr[-1])

        2,3,4,5,9,11,14,11 k = 3 x = 4
        2, 1, 0
        1, 0, 1
        0, 1, 5
        """


        left = 0
        sum = 0
        for i in range(k):
            sum += abs(arr[i] - x)

        minSum = sum
        ans = arr[:k]
        for right in range(k, len(arr)):
            sum -= abs(arr[left] - x)
            sum += abs(arr[right] - x)
            left += 1
            print(sum)
            if sum < minSum:
                minSum = sum
                ans = arr[left: right + 1]
        return ans