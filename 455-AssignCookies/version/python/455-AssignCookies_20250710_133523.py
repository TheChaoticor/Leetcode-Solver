# Last updated: 7/10/2025, 1:35:23 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()

        r,l = 0,0
        while l<m and r<n:
            if g[r]<=s[l]:
                r+=1
            l += 1
        
        return r
