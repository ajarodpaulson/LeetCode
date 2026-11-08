class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        acc = []
        self.subsetXORSumHelper(nums, [], acc)

        xor_sum = 0
        for i in range(len(acc)):
            xor_sum_subset = 0
            for j in range(len(acc[i])):
                xor_sum_subset = xor_sum_subset ^ acc[i][j]
            xor_sum = xor_sum + xor_sum_subset

        return xor_sum


    def subsetXORSumHelper(self, nums: List[int], curr_subset: List[int], acc: List[List[int]]):
        if not nums:
            acc.append(curr_subset)
            return

        curr_subset_include = curr_subset + [nums[0]]
        curr_subset_exclude = curr_subset
        self.subsetXORSumHelper(nums[1:], curr_subset_include, acc)
        self.subsetXORSumHelper(nums[1:], curr_subset_exclude, acc)
        
