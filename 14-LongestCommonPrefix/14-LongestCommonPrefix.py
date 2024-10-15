class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a,b=max(strs),min(strs)
        return max({b[:i] for i in range(len(b)+1)} & 
					{a[:i] for i in range(len(a)+1)}, key=len)
