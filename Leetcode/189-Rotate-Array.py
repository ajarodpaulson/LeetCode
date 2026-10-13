class Solution:
    def reverse_list(self, nums: list[int], start_idx: int, end_idx: int):
        while start_idx < end_idx:
            nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
            start_idx += 1
            end_idx -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        adjusted_k = k % len(nums)
        nums.reverse()
        self.reverse_list(nums, 0, adjusted_k-1)
        self.reverse_list(nums, adjusted_k, len(nums) -1)




    
        