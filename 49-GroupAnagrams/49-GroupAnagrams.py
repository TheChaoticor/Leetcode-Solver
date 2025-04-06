# Last updated: 4/6/2025, 7:51:02 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls=defaultdict(list)
        for i in strs:
            l="".join(sorted(i))
            ls[l].append(i)
        return list(ls.values())

               
        