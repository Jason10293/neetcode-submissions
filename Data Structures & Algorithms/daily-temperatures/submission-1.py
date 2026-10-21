class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        stk = []
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prev_index = stk.pop()
                ans[prev_index] = index - prev_index
            stk.append(index)
            

        return ans



