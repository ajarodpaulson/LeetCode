class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        def getIsAlternatingGroup(curr_window: List[int]):
            last = curr_window[0]
            for i in range(1, len(curr_window)):
                if last == curr_window[i]:
                    return False
                last = curr_window[i]
            return True
        start, end = 0, 0
        output = 0
        while end < len(colors) + 2:
            if end - start + 1 > 3:
                start += 1

            if end - start + 1 == 3:
                curr_window = [colors[(start + i) % len(colors)] for i in range(end - start + 1)]
                output = output + 1 if getIsAlternatingGroup(curr_window) else output

            end += 1

        return output
        