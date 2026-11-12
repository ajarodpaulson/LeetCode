class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        end_window = k
        min_difference = float(inf)

        while end_window <= len(nums):
            min_difference = min(min_difference, nums[end_window - 1] - nums[end_window - k])
            end_window += 1
    
        return min_difference
'''
Time: nlogn for the sort + a loop that repeats roughly n times => O(nlogn)
Space: O(1)
'''
