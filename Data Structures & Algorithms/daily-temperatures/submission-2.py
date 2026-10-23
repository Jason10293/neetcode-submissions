class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                ans[stk[-1]] = index - stk[-1]
                stk.pop()
            stk.append(index)
        return ans