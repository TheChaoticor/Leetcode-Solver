# Last updated: 6/30/2025, 9:10:12 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)

        return nums
