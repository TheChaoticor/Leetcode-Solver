# Last updated: 6/19/2025, 11:03:26 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs==[""]:
            return [[""]]


            

        
        lst=defaultdict(list)
        for word in strs:
            sorw=''.join(sorted(word))
            lst[sorw].append(word)
        return list(lst.values())
