1from typing import List
2
3class Solution:
4    def separateDigits(self, nums: List[int]) -> List[int]:
5        answer = []
6        
7        for num in nums:
8            # Convert the integer to string to iterate over each digit
9            for digit_char in str(num):
10                # Convert the character back to integer and append to answer
11                answer.append(int(digit_char))
12        
13        return answer