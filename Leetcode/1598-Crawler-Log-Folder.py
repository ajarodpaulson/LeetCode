'''
  V
["d1/","d2/","./","d3/","../","d31/"] 0
        V
["d1/","d2/","./","d3/","../","d31/"] 1
              V
["d1/","d2/","./","d3/","../","d31/"] 2
                    V
["d1/","d2/","./","d3/","../","d31/"] 2
                          V
["d1/","d2/","./","d3/","../","d31/"] 3
                                V
["d1/","d2/","./","d3/","../","d31/"] 2
                                     V
["d1/","d2/","./","d3/","../","d31/"] 3

'''
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        levels_deep = 0
        for log in logs:
            if (log == "../"):
                levels_deep = levels_deep if levels_deep == 0 else levels_deep - 1
            elif (log == "./"):
                continue
            else: # move into a child folder
                levels_deep += 1

        return levels_deep
        