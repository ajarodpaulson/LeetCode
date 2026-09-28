class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        min = nums[0] if nums[0] < nums[1] else nums[1]
        max = nums[0] if nums[0] > nums[1] else nums[1]

        if nums[2] > min and nums[2] < max:
            return nums[2]

        elif nums[2] > min:
            return max

        else:
            return min