1'''
2v
31 2 3 | 
4  v
51 2 3 | [[1], [1, 2], [2]]
6    v
71 2 3 | [[1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]
8
9so what it looks to me is
10if we iterate over nums
11at the ith index, we will have i subsets that we need to build on, plus we need to add the newest one unless its an element we've already seen
12
13plan
14- iterate over nums
15- at each index i,
16    - create i new lists and add nums[i] to each of them
17    - create an additional list with nums[i] unless it has already been seen
18- continue to end
19
20nums = [0]
21
22'''
23class Solution:
24    def subsets(self, nums: List[int]) -> List[List[int]]:
25        output = [[]]
26
27        for i, num in enumerate(nums):
28            for j in range(len(output)):
29                next_set = output[j] + [num]
30                output.append(next_set)
31
32        return output