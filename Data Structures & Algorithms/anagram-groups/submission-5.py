from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for elem in strs:
            groups["".join(sorted(elem))].append(elem)
        return list(groups.values())