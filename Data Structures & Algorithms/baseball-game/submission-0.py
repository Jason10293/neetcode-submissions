class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk  = []
        for op in operations:
            if op == "+":
                stk.append(stk[-2] + stk[-1])
            elif op == "C":
                stk.pop()
            elif op == "D":
                stk.append(2 * stk[-1])
            else:
                stk.append(int(op))
        
        sum = 0
        while stk:
            sum += stk.pop()
        
        return sum