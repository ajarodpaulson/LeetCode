class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        p2 = 2

        while p1 < len(nums):
            if nums[p1] > nums[p1-1]:
                p1 += 1
                continue
            
            if not p2 < len(nums):
                break

            if nums[p2] > nums[p1 - 1]:
                nums[p1] = nums[p2]
                p1 += 1

            p2 += 1

        return p1
