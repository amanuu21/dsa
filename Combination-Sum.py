1from typing import List
2
3class Solution:
4    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
5        res = []
6
7        def backtrack(start, path, remaining):
8            if remaining == 0:
9                res.append(path[:])
10                return
11            if remaining < 0:
12                return
13
14            for i in range(start, len(candidates)):
15                # choose
16                path.append(candidates[i])
17
18                # stay on same index (reuse allowed)
19                backtrack(i, path, remaining - candidates[i])
20
21                # undo choice
22                path.pop()
23
24        backtrack(0, [], target)
25        return res