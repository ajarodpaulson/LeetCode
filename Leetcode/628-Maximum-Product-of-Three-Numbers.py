class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        
        product_of_last_3 = nums[-3] * nums[-2] * nums[-1]
        product_of_first_2_and_last = nums[0] * nums[1] * nums[-1]

        return product_of_last_3 if product_of_last_3 > product_of_first_2_and_last else product_of_first_2_and_last
        