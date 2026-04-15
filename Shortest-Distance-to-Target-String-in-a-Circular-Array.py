1class Solution:
2    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
3        n = len(words)
4        min_distance = float('inf')
5
6        for i in range(n):
7            if words[i] == target:
8                distance = abs(i - startIndex)
9                min_distance = min(min_distance, distance, n - distance)
10
11        return min_distance if min_distance != float('inf') else -1