class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()

        return -1 if len(nums) < 3 else nums[1]