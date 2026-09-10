class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0 # first occurrence
        p2 = 0

        while p2 - p1 < len(needle) and p2 < len(haystack):
            if (haystack[p2] == needle[p2 - p1]):
                p2 += 1
            else:
                p1 += 1
                p2 = p1

        if p2 - p1 == len(needle):
            return p1
        else:
            return -1

            
        