# Last updated: 5/20/2025, 11:19:42 PM
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nt = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))  # Sorted word is the same for all anagrams
            nt[key].append(word)
        return list(nt.values())
