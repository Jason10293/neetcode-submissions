class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_array = []
        for i in range(len(matrix)):
            prefix = [0]
            running_sum = 0
            for j in range(len(matrix[0])):
                running_sum += matrix[i][j]
                prefix.append(running_sum)
            self.prefix_array.append(prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = col1
        right = col2

        top = row1
        bottom = row2   

        ans = 0
        for row in range(top, bottom + 1):
            ans += self.prefix_array[row][right + 1] - self.prefix_array[row][left]

        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)