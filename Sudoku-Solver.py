1class Solution:
2    def solveSudoku(self, board: list[list[str]]) -> None:
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6        empty = []
7        
8        # Initialize
9        for r in range(9):
10            for c in range(9):
11                if board[r][c] == '.':
12                    empty.append((r, c))
13                else:
14                    val = board[r][c]
15                    rows[r].add(val)
16                    cols[c].add(val)
17                    boxes[(r//3)*3 + (c//3)].add(val)
18        
19        def backtrack():
20            if not empty:
21                return True
22            
23            # 🔥 MRV: choose cell with fewest options
24            min_options = 10
25            best_idx = -1
26            
27            for i, (r, c) in enumerate(empty):
28                box = (r//3)*3 + (c//3)
29                options = 0
30                
31                for num in "123456789":
32                    if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
33                        options += 1
34                
35                if options < min_options:
36                    min_options = options
37                    best_idx = i
38            
39            r, c = empty.pop(best_idx)
40            box = (r//3)*3 + (c//3)
41            
42            for num in "123456789":
43                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
44                    
45                    board[r][c] = num
46                    rows[r].add(num)
47                    cols[c].add(num)
48                    boxes[box].add(num)
49                    
50                    if backtrack():
51                        return True
52                    
53                    # undo
54                    board[r][c] = '.'
55                    rows[r].remove(num)
56                    cols[c].remove(num)
57                    boxes[box].remove(num)
58            
59            empty.insert(best_idx, (r, c))
60            return False
61        
62        backtrack()