class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = float(-inf)
        second_largest = float(-inf)
        largest_idx = None
        for idx, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                largest_idx = idx
            elif num > second_largest:
                second_largest = num
        if second_largest * 2 <= largest:
            return largest_idx
        else:
            return -1
