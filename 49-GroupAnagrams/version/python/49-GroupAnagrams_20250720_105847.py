# Last updated: 7/20/2025, 10:58:47 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs==[""]:
            return [[""]]

        dic=defaultdict(list)
        for word in strs:
            sorw=''.join(sorted(word))
            dic[sorw].append(word)

        return list(dic.values())   

        