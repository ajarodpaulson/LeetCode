1class Solution {
2    func minLength(_ s: String) -> Int {
3        var stack: Array<Character> = Array()
4
5        let dcArray: Array<Character> = Array(["D", "C"])
6        let baArray: Array<Character> = Array(["B", "A"])
7
8        for c in s {
9            if let last = stack.last {
10                let charArray: Array<Character> = Array([c, last])
11
12                if (charArray == dcArray || charArray == baArray) {
13                    stack.popLast()
14                } else {
15                    stack.append(c)
16                }
17            } else {
18                stack.append(c)
19            }
20        }
21
22        return stack.count
23    }
24}