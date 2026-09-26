class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_remaining = self.getStrAfterTyping(s)
        t_remaining = self.getStrAfterTyping(t)

        print('s_remaining', s_remaining)
        print('t_remaining', t_remaining)
        return s_remaining == t_remaining

    
    def getStrAfterTyping(self, raw_str: str) -> str:
        str_backspaces = 0
        str_remaining = ''

        for c in reversed(raw_str):
            if (c == '#'):
                str_backspaces += 1
                continue
            
            if str_backspaces > 0:
                str_backspaces -= 1
                continue

            str_remaining += c

        return str_remaining
    


            

        