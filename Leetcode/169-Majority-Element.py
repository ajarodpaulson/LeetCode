class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq_by_num = {}
        for num in nums:
            freq_by_num[num] = freq_by_num.get(num, 0) + 1

        for num, freq in freq_by_num.items():
            if freq > (len(nums) / 2):
                return num
        