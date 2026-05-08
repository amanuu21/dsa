1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        # Strip trailing spaces and split into words
4        words = s.strip().split()
5        # Return the length of the last word
6        return len(words[-1]) if words else 0