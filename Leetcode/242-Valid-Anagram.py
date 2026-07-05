class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict_s = {}

        for c in s:
            count_c = freq_dict_s.get(c, 0)
            freq_dict_s[c] = count_c + 1

        freq_dict_t = {}

        for c in t:
            count_c = freq_dict_t.get(c, 0)
            freq_dict_t[c] = count_c + 1

        return freq_dict_s == freq_dict_t