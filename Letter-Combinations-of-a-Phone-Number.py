1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if not digits:
4            return []
5
6        phone = {
7            "2": "abc", "3": "def", "4": "ghi",
8            "5": "jkl", "6": "mno", "7": "pqrs",
9            "8": "tuv", "9": "wxyz"
10        }
11
12        result = []
13
14        def backtrack(index, path):
15            if index == len(digits):
16                result.append(path)
17                return
18
19            for letter in phone[digits[index]]:
20                backtrack(index + 1, path + letter)
21
22        backtrack(0, "")
23        return result