1class Solution:
2    def subsetXORSum(self, nums: List[int]) -> int:
3        def get_subsets(current_idx: int, current_path: list[int], all_subsets: List[List[int]]):
4            # if the current index is out of bounds we're done 
5            if (current_idx >= len(nums)):
6                all_subsets.append(current_path.copy())
7                return
8
9            get_subsets(current_idx + 1, current_path, all_subsets) # exclude path
10
11            current_path.append(nums[current_idx])
12            get_subsets(current_idx + 1, current_path, all_subsets) # include path
13            current_path.pop()
14
15        all_subsets = []
16        get_subsets(0, [], all_subsets)
17
18        running_sum_total = 0
19        for subset in all_subsets:
20            running_sum_subset = 0
21            for num in subset:
22                running_sum_subset = running_sum_subset ^ num
23
24            running_sum_total = running_sum_total + running_sum_subset
25
26        return running_sum_total
27
28
29            
30        
31
32        
33                
34
35        