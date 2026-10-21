class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        28
        49
        35
        36
        30
        38
        30


        have a stack
        if empty or element < top elelemt --> push
        while element > top element pop
        for every element popped append to array
        pad the rest of the aray with 0's
        """


        stk = []
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prev_index = stk.pop()
                ans[prev_index] = index - prev_index
            stk.append(index)
            

        return ans



