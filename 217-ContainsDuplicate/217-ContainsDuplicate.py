class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsdict=Counter(nums)
        for i in numsdict.keys():
            if numsdict[i]>=2:
                return True
        return False

        