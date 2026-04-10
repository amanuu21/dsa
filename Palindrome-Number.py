1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        
6        original = x
7        reversed_num = 0
8        
9        while x != 0:
10            digit = x % 10
11            reversed_num = reversed_num * 10 + digit
12            x //= 10
13        
14        return original == reversed_num