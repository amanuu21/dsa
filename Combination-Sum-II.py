1from typing import List
2
3class Solution:
4    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
5        candidates.sort()
6        res = []
7
8        def backtrack(start, path, remaining):
9            if remaining == 0:
10                res.append(path[:])
11                return
12            if remaining < 0:
13                return
14
15            for i in range(start, len(candidates)):
16                # skip duplicates
17                if i > start and candidates[i] == candidates[i - 1]:
18                    continue
19
20                # choose
21                path.append(candidates[i])
22
23                # move forward (no reuse)
24                backtrack(i + 1, path, remaining - candidates[i])
25
26                # undo
27                path.pop()
28
29        backtrack(0, [], target)
30        return res