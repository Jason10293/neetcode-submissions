class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Use binary search
        left = 0
        right = num
        mid = num / 2 --> float
        if mid^2 > num --> mid = right
        else mid^2 < num --> mid = left
        end if abs(mid ^ 2 - num) < 0.00001
        return int(mid)
        """

        left = 0
        right = x
        mid = right
        while True:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x and (mid + 1) ** 2 > x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1

