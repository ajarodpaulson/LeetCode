'''
[-1, 2, 1, -4] t = 1
[-4, -1, 1, 2] t = 1  s = -4 + -1 + 2 = -3 closest = -3
  i   l     r
[-4, -1, 1, 2] t = 1  
  i      l  r

target = 5
closest = 3
current = 2
'''
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = float('inf')
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_nums = nums[i] + nums[left] + nums[right]

                if sum_nums == target:
                    return sum_nums

                if sum_nums < target:
                    if abs(target-sum_nums) < abs(target-closest):
                        closest = sum_nums
                    left += 1

                else:
                    if abs(target-sum_nums) < abs(target-closest):
                        closest = sum_nums
                    right -= 1

        return closest

