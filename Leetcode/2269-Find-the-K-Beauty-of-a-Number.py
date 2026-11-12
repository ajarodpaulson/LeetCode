class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        start = 0
        end = start + k - 1
        output = 0
        num_str = str(num)
        while end < len(num_str):
            substring_int = int(num_str[start:end+1])
            if substring_int == 0:
                start += 1
                end = start + k - 1
                continue

            remainder = num % substring_int
            if remainder == 0:
                output += 1

            start += 1
            end = start + k - 1
        return output
'''
time: the while loop repeats roughly n times, with constant time work during the body of each loop => O(n)
space: O(1) since local variables all have constant space
'''
        