1class Solution:
2    def minimumDistance(self, word: str) -> int:
3        # Convert letter to (row, col)
4        def get_pos(c):
5            idx = ord(c) - ord('A')
6            return (idx // 6, idx % 6)
7
8        # Distance between two letters
9        def dist(a, b):
10            if a is None or b is None:
11                return 0
12            x1, y1 = get_pos(a)
13            x2, y2 = get_pos(b)
14            return abs(x1 - x2) + abs(y1 - y2)
15
16        from functools import lru_cache
17
18        @lru_cache(None)
19        def dp(i, f1, f2):
20            # i = current index in word
21            # f1, f2 = current positions of fingers (letters or None)
22            
23            if i == len(word):
24                return 0
25
26            # Option 1: use finger 1
27            use_f1 = dist(f1, word[i]) + dp(i + 1, word[i], f2)
28
29            # Option 2: use finger 2
30            use_f2 = dist(f2, word[i]) + dp(i + 1, f1, word[i])
31
32            return min(use_f1, use_f2)
33
34        return dp(0, None, None)