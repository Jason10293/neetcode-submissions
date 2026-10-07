from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for elem in strs:
            freq = [0] * 26
            for char in elem:
                index = ord(char) - 97
                freq[index] += 1
            
            groups[tuple(freq)].append(elem)
        return list(groups.values())