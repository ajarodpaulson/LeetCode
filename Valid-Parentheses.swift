1class Solution {
2    func isValid(_ s: String) -> Bool {
3        var stack: Array<Character> = Array()
4
5        for c in s {
6           if let last = stack.last {
7            if isCounterpart(last, c) {
8                stack.popLast()
9            } else {
10                stack.append(c)
11            }
12           } else {
13            stack.append(c)
14           }
15        }
16
17        return stack.isEmpty 
18    }
19
20    func isCounterpart(_ c1: Character, _ c2: Character) -> Bool {
21        let charSet: Array = [c1, c2]
22
23        return charSet == Array<Character>(["(", ")"]) || charSet == Array<Character>(["[", "]"]) || charSet == Array<Character>(["{", "}"])
24    }
25}