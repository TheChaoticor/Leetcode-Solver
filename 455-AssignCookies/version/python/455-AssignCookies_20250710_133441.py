# Last updated: 7/10/2025, 1:34:41 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        k=0
        g=sorted(g)
        s=sorted(s)
        i=0
        j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
            j+=1    

        return i            
