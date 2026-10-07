from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            groups[sorted_str].append(str)
        
        ans = []
        for (key, value) in groups.items():
            ans.append(value)
        
        return ans