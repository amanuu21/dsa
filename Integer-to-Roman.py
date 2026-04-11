1class Solution:
2    def intToRoman(self, num: int) -> str:
3        values = [
4            1000, 900, 500, 400,
5            100, 90, 50, 40,
6            10, 9, 5, 4,
7            1
8        ]
9        
10        symbols = [
11            "M", "CM", "D", "CD",
12            "C", "XC", "L", "XL",
13            "X", "IX", "V", "IV",
14            "I"
15        ]
16        
17        result = ""
18        
19        for i in range(len(values)):
20            while num >= values[i]:
21                result += symbols[i]
22                num -= values[i]
23        
24        return result