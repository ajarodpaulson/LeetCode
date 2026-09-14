class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_dict = {}

        for c in s:
            freq_dict[c] = freq_dict.get(c, 0) + 1
        
        for c in t:
            freq_dict[c] = freq_dict.get(c, 0) - 1

        for key, value in freq_dict.items():
            if value == -1:
                return key

    