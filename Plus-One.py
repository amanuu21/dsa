1from typing import List
2
3class Solution:
4    def plusOne(self, digits: List[int]) -> List[int]:
5        # Start from the last digit (least significant)
6        for i in range(len(digits) - 1, -1, -1):
7            # If current digit is less than 9, just increment and return
8            if digits[i] < 9:
9                digits[i] += 1
10                return digits
11            # If current digit is 9, set it to 0 and continue to next digit
12            digits[i] = 0
13        
14        # If we're here, all digits were 9 (e.g., [9,9,9])
15        # Need to add a 1 at the beginning
16        return [1] + digits