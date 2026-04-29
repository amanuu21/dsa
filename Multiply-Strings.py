1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        if num1 == "0" or num2 == "0":
4            return "0"
5        
6        n, m = len(num1), len(num2)
7        res = [0] * (n + m)
8        
9        # multiply from right to left
10        for i in range(n - 1, -1, -1):
11            for j in range(m - 1, -1, -1):
12                mul = int(num1[i]) * int(num2[j])
13                
14                # position in result
15                p1, p2 = i + j, i + j + 1
16                
17                total = mul + res[p2]
18                
19                res[p2] = total % 10
20                res[p1] += total // 10
21        
22        # convert to string
23        result = ''.join(map(str, res))
24        
25        # remove leading zeros
26        return result.lstrip('0')