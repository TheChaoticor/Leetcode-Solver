# Last updated: 4/6/2025, 8:36:41 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        dic=dict(sorted(dic.items(),key= lambda item:item[1],reverse=True))
        
        ls=[]
        c=0
        for i in dic:
            if c==k:
                break
            ls.append(i)
            c+=1
        return ls        