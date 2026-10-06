'''
[1,0,-1,0,-2,2]
 i   j   l        r
[-2, -1, 0, 0, 1, 2]   -2 + -1 + 0 + 2 = -1
i    j         l   r
[-2, -1, 0, 0, 1, 2]   sum = 0
i        j  l     r
[-2, -1, 0, 0, 1, 2]   sum = 0

 i   j    l     r
[-2, -1, -1, 1, 1]    target == -1
 i   j       l  r
[-2, -1, -1, 1, 1]    target == -1  [-2, -1, 1, 1]
 i       j   l  r
[-2, -1, -1, 1, 1]    target == -1  [-2, -1, 1, 1]
[1, 1, 1, 1]
 i  j
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1

                        while nums[left - 1] == nums[left] and left < right:
                            left += 1

                        right -= 1

                        while nums[right] == nums[right + 1] and left < right:
                            right -= 1
                    
                    elif sum < target:
                        left += 1

                    else:
                        right -= 1

        return output