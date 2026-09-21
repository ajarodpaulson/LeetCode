class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = [float(-inf), float(-inf)] # value, idx
        second_largest = [float(-inf), float(-inf)]

        for idx, num in enumerate(nums):
            if num > largest[0]:
                second_largest[0] = largest[0]
                second_largest[1] = largest[1]
                largest[0] = num
                largest[1] = idx
            elif num > second_largest[0]:
                second_largest[0] = num
                second_largest[1] = idx

        return largest[1] if second_largest[0] * 2 <= largest[0] else -1
        