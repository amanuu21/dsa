1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        # Convert binary strings to integers, add them, then convert back to binary
4        # int(a, 2) means "interpret string 'a' as base-2 (binary) number"
5        # bin() returns a string like '0b101' so we slice off the '0b' prefix
6        return bin(int(a, 2) + int(b, 2))[2:]