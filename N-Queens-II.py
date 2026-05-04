1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        """
4        Returns the number of distinct solutions to the n-queens puzzle.
5        """
6        self.count = 0
7        self.n = n
8        
9        # Sets to track occupied columns and diagonals
10        cols = set()           # column index
11        diag1 = set()          # (r + c) for '/' diagonal
12        diag2 = set()          # (r - c) for '\' diagonal
13        
14        def backtrack(row: int):
15            if row == self.n:
16                self.count += 1
17                return
18            
19            for col in range(self.n):
20                if col in cols or (row + col) in diag1 or (row - col) in diag2:
21                    continue
22                
23                # Place queen
24                cols.add(col)
25                diag1.add(row + col)
26                diag2.add(row - col)
27                
28                # Recurse to next row
29                backtrack(row + 1)
30                
31                # Remove queen (backtrack)
32                cols.remove(col)
33                diag1.remove(row + col)
34                diag2.remove(row - col)
35        
36        backtrack(0)
37        return self.count