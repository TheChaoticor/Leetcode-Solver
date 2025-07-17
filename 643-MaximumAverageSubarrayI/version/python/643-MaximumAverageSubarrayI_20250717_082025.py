# Last updated: 7/17/2025, 8:20:25 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=0
        max=float('-inf')
        sd=[]
        if s=="":
            return 0

        for i in range(len(s)):
            v=''.join(sd)
            if s[i] not in sd :
                c+=1
                sd.append(s[i])
                if c>max:
                    max=c
            else:
                while s[i] in sd:
                    sd.pop(0)
                    c -= 1
                sd.append(s[i])
                c += 1
                if c > max:
                    max = c        
        return max if max else 0       

