1class Solution:
2    def countAndSay(self, n: int) -> str:
3        res = "1"
4        
5        for _ in range(n - 1):
6            i = 0
7            new_res = ""
8            
9            while i < len(res):
10                count = 1
11                
12                # count consecutive characters
13                while i + 1 < len(res) and res[i] == res[i + 1]:
14                    i += 1
15                    count += 1
16                
17                new_res += str(count) + res[i]
18                i += 1
19            
20            res = new_res
21        
22        return res