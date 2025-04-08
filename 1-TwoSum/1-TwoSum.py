# Last updated: 4/8/2025, 11:01:59 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls=set(nums)
        lolng=0
        for num in ls:
            if num-1 not in ls:
                curr=num
                c=1
                while curr+1 in ls:
                    c+=1
                    curr+=1
                lolng=max(lolng,c)

        return lolng            