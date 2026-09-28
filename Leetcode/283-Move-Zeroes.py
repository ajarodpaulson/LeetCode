'''

'''
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slowptr = 0
        fastptr = 0

        while slowptr < len(nums) and fastptr < len(nums):
            if nums[slowptr] != 0:
                slowptr += 1
                fastptr = slowptr
            else:
                while fastptr < len(nums):
                    if nums[fastptr] == 0:
                        fastptr += 1
                    else:
                        nums[slowptr] = nums[fastptr]
                        nums[fastptr] = 0
                        slowptr += 1
        return nums

        