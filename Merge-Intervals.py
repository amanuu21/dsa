1from typing import List
2
3class Solution:
4    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
5        if not intervals:
6            return []
7
8        # Sort intervals by start time
9        intervals.sort(key=lambda x: x[0])
10
11        merged = []
12        current_start, current_end = intervals[0]
13
14        for start, end in intervals[1:]:
15            if start <= current_end:  # Overlapping
16                current_end = max(current_end, end)  # Merge
17            else:
18                merged.append([current_start, current_end])  # Add previous
19                current_start, current_end = start, end  # Move to next interval
20
21        # Add the last interval
22        merged.append([current_start, current_end])
23
24        return merged