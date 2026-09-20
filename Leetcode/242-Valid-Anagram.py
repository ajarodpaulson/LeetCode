class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_by_char = {}

        for c in s:
            freq_by_char[c] = freq_by_char.get(c, 0) + 1
        
        for c in t:
            freq_by_char[c] = freq_by_char.get(c, 0) - 1
        
        for v in freq_by_char.values():
            if v != 0:
                return False

        return True