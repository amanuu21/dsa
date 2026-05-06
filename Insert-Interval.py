1from typing import List
2
3class Solution:
4    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
5        result = []
6        i = 0
7        n = len(intervals)
8
9        # Add all intervals that end before newInterval starts
10        while i < n and intervals[i][1] < newInterval[0]:
11            result.append(intervals[i])
12            i += 1
13
14        # Merge overlapping intervals
15        while i < n and intervals[i][0] <= newInterval[1]:
16            newInterval[0] = min(newInterval[0], intervals[i][0])
17            newInterval[1] = max(newInterval[1], intervals[i][1])
18            i += 1
19        result.append(newInterval)
20
21        # Add remaining intervals
22        while i < n:
23            result.append(intervals[i])
24            i += 1
25
26        return result