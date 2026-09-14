class Solution:
    '''
    [1] -> 1
    [1, 2] -> 2
    [1, 2, 3] -> 1
    [-1, -2] -> -1
    [-1, -2, -3] -> -3
    [-1, -2, 1, 2, 3] -> 1
    [-1, -2, 2, 2, 3] -> -1
    '''
    def thirdMax(self, nums: List[int]) -> int:
        first_max = float(-inf)
        second_max = float(-inf)
        third_max = float(-inf)

        def bubbleValsDown(self, num_to_insert, insert_position):
            nonlocal first_max
            nonlocal second_max
            nonlocal third_max
            match (insert_position):
                case 'first':
                    third_max = second_max
                    second_max = first_max
                    first_max = num_to_insert
                case 'second':
                    third_max = second_max
                    second_max = num_to_insert
                case 'third':
                    third_max = num_to_insert
        
        for num in nums:
            if num == first_max or num == second_max or num == third_max:
                continue
            if num > first_max:
                bubbleValsDown(self, num, 'first')
            elif num > second_max:
                bubbleValsDown(self, num, 'second')
            elif num > third_max:
                bubbleValsDown(self, num, 'third')

        if third_max == float(-inf):
            return first_max
        else:
            return third_max

    

        


            

        