from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for elem in strs:
            freq = [0] * 26
            for char in elem:
                index = ord(char) - 97
                freq[index] += 1
            freq_str = ",".join(map(str, freq))
            groups[freq_str].append(elem)
        ans = []
        for value in groups.values():
            ans.append(value)
        
        return ans