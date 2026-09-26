class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        g_ptr = 0
        s_ptr = 0

        while g_ptr < len(g) and s_ptr < len(s):
            curr_child_greed = g[g_ptr]
            curr_cookie_size = s[s_ptr]

            if curr_child_greed <= curr_cookie_size:
                g_ptr += 1
                s_ptr += 1

            else:
                s_ptr += 1

        return g_ptr

        