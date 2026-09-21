class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count_less_than_by_num = {}

        nums_copy = nums.copy()
        nums_copy.sort()
        sorted_nums = nums_copy

        last_value = sorted_nums[0]
        count_less_than_by_num[sorted_nums[0]] = 0

        for i in range(1, len(sorted_nums)):
            curr_num = sorted_nums[i]
            if curr_num == last_value:
                last_value = curr_num
                continue

            count_less_than_by_num[curr_num] = i
            last_value = curr_num

        return_value = []

        for num in nums:
            return_value.append(count_less_than_by_num[num])

        return return_value