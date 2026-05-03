1from typing import List
2
3class Solution:
4    def solveNQueens(self, n: int) -> List[List[str]]:
5        result = []
6        
7        # Chessboard representation (row to column mapping)
8        # queens[row] = column where queen is placed
9        queens = [-1] * n
10        
11        # Sets to track occupied columns and diagonals
12        cols = set()           # occupied columns
13        diag1 = set()          # occupied diagonals (r + c) - top-left to bottom-right
14        diag2 = set()          # occupied diagonals (r - c) - top-right to bottom-left
15        
16        def backtrack(row: int):
17            # If we've placed queens in all rows, we found a solution
18            if row == n:
19                # Convert the solution to the required board format
20                board = self._create_board(queens, n)
21                result.append(board)
22                return
23            
24            # Try placing a queen in each column of the current row
25            for col in range(n):
26                # Check if the position is under attack
27                if col in cols or (row + col) in diag1 or (row - col) in diag2:
28                    continue
29                
30                # Place the queen
31                queens[row] = col
32                cols.add(col)
33                diag1.add(row + col)
34                diag2.add(row - col)
35                
36                # Recurse to the next row
37                backtrack(row + 1)
38                
39                # Backtrack: remove the queen
40                cols.remove(col)
41                diag1.remove(row + col)
42                diag2.remove(row - col)
43                queens[row] = -1
44        
45        # Start backtracking from the first row
46        backtrack(0)
47        return result
48    
49    def _create_board(self, queens: List[int], n: int) -> List[str]:
50        """Convert queen positions to board representation"""
51        board = []
52        for row in range(n):
53            # Create a row with '.' in all columns
54            row_chars = ['.'] * n
55            # Place 'Q' at the queen's column for this row
56            row_chars[queens[row]] = 'Q'
57            # Join the characters to form a string
58            board.append(''.join(row_chars))
59        return board
60
61
62# Alternative implementation with board built directly (less efficient but more intuitive)
63class SolutionBoard:
64    def solveNQueens(self, n: int) -> List[List[str]]:
65        result = []
66        board = [['.' for _ in range(n)] for _ in range(n)]
67        
68        def is_safe(row: int, col: int) -> bool:
69            # Check column above
70            for i in range(row):
71                if board[i][col] == 'Q':
72                    return False
73            
74            # Check upper-left diagonal
75            i, j = row - 1, col - 1
76            while i >= 0 and j >= 0:
77                if board[i][j] == 'Q':
78                    return False
79                i -= 1
80                j -= 1
81            
82            # Check upper-right diagonal
83            i, j = row - 1, col + 1
84            while i >= 0 and j < n:
85                if board[i][j] == 'Q':
86                    return False
87                i -= 1
88                j += 1
89            
90            return True
91        
92        def backtrack(row: int):
93            if row == n:
94                # Convert board to list of strings
95                result.append([''.join(row_chars) for row_chars in board])
96                return
97            
98            for col in range(n):
99                if is_safe(row, col):
100                    # Place queen
101                    board[row][col] = 'Q'
102                    # Recurse
103                    backtrack(row + 1)
104                    # Backtrack
105                    board[row][col] = '.'
106        
107        backtrack(0)
108        return result
109
110
111# Test cases
112if __name__ == "__main__":
113    solution = Solution()
114    
115    # Test with n = 4
116    print("Solutions for n = 4:")
117    solutions = solution.solveNQueens(4)
118    for i, sol in enumerate(solutions):
119        print(f"Solution {i + 1}:")
120        for row in sol:
121            print(row)
122        print()
123    
124    # Test with n = 1
125    print("Solutions for n = 1:")
126    solutions = solution.solveNQueens(1)
127    for sol in solutions:
128        print(sol)
129    
130    # Expected output for n = 4: 2 solutions
131    # [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]