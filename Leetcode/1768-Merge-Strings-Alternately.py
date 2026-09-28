class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0

        merged = ""
        while p1 < len(word1) or p2 < len(word2):
            if not p1 < len(word1):
                merged = merged + word2[p2]
                p2 += 1
                continue
            elif not p2 < len(word2):
                merged = merged + word1[p1]
                p1 += 1
                continue
            else:
                if p1 <= p2:
                    merged = merged + word1[p1]
                    p1 += 1
                else:
                    merged = merged + word2[p2]
                    p2 += 1

        return merged

        