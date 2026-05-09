1from typing import List
2
3class Solution:
4    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
5        m, n = len(grid), len(grid[0])
6        
7        # Number of layers
8        layers = min(m, n) // 2
9        
10        for layer in range(layers):
11            # Extract the layer elements in order (clockwise)
12            elements = []
13            
14            # Top row (left to right)
15            for j in range(layer, n - layer):
16                elements.append(grid[layer][j])
17            
18            # Right column (top to bottom, excluding top corner)
19            for i in range(layer + 1, m - layer):
20                elements.append(grid[i][n - layer - 1])
21            
22            # Bottom row (right to left, excluding right corner)
23            for j in range(n - layer - 2, layer - 1, -1):
24                elements.append(grid[m - layer - 1][j])
25            
26            # Left column (bottom to top, excluding bottom and top corners)
27            for i in range(m - layer - 2, layer, -1):
28                elements.append(grid[i][layer])
29            
30            # Calculate effective rotation (counter-clockwise = move elements backward)
31            # If k=1, the element at position 1 goes to position 0
32            rotation = k % len(elements)
33            
34            # Rotate counter-clockwise
35            if rotation > 0:
36                elements = elements[rotation:] + elements[:rotation]
37            
38            # Put elements back in clockwise order
39            idx = 0
40            
41            # Top row
42            for j in range(layer, n - layer):
43                grid[layer][j] = elements[idx]
44                idx += 1
45            
46            # Right column
47            for i in range(layer + 1, m - layer):
48                grid[i][n - layer - 1] = elements[idx]
49                idx += 1
50            
51            # Bottom row
52            for j in range(n - layer - 2, layer - 1, -1):
53                grid[m - layer - 1][j] = elements[idx]
54                idx += 1
55            
56            # Left column
57            for i in range(m - layer - 2, layer, -1):
58                grid[i][layer] = elements[idx]
59                idx += 1
60        
61        return grid
62
63
64# Alternative implementation with clearer rotation logic
65class SolutionAlternate:
66    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
67        m, n = len(grid), len(grid[0])
68        layers = min(m, n) // 2
69        
70        for layer in range(layers):
71            # Get all elements in current layer in clockwise order
72            elements = []
73            
74            # Collect elements clockwise
75            # Top edge
76            for j in range(layer, n - layer):
77                elements.append(grid[layer][j])
78            
79            # Right edge
80            for i in range(layer + 1, m - layer):
81                elements.append(grid[i][n - layer - 1])
82            
83            # Bottom edge (reverse)
84            if m - layer - 1 > layer:
85                for j in range(n - layer - 2, layer - 1, -1):
86                    elements.append(grid[m - layer - 1][j])
87            
88            # Left edge (reverse)
89            if n - layer - 1 > layer:
90                for i in range(m - layer - 2, layer, -1):
91                    elements.append(grid[i][layer])
92            
93            # Rotate counter-clockwise (move first 'k' elements to the end)
94            # For counter-clockwise rotation, we want elements[k:] + elements[:k]
95            rotation = k % len(elements)
96            if rotation > 0:
97                elements = elements[rotation:] + elements[:rotation]
98            
99            # Place elements back in clockwise order
100            idx = 0
101            
102            # Top edge
103            for j in range(layer, n - layer):
104                grid[layer][j] = elements[idx]
105                idx += 1
106            
107            # Right edge
108            for i in range(layer + 1, m - layer):
109                grid[i][n - layer - 1] = elements[idx]
110                idx += 1
111            
112            # Bottom edge
113            if m - layer - 1 > layer:
114                for j in range(n - layer - 2, layer - 1, -1):
115                    grid[m - layer - 1][j] = elements[idx]
116                    idx += 1
117            
118            # Left edge
119            if n - layer - 1 > layer:
120                for i in range(m - layer - 2, layer, -1):
121                    grid[i][layer] = elements[idx]
122                    idx += 1
123        
124        return grid
125
126
127# Test cases
128if __name__ == "__main__":
129    solution = Solution()
130    
131    # Test case 1: 2x2 matrix
132    grid1 = [[40, 10], [30, 20]]
133    print("Input:", grid1)
134    print("k = 1")
135    result1 = solution.rotateGrid([row[:] for row in grid1], 1)
136    print("Output:", result1)
137    print("Expected: [[10,20],[40,30]]")
138    print()
139    
140    # Test case 2: 4x4 matrix
141    grid2 = [
142        [1, 2, 3, 4],
143        [5, 6, 7, 8],
144        [9, 10, 11, 12],
145        [13, 14, 15, 16]
146    ]
147    print("Input:")
148    for row in grid2:
149        print(row)
150    print("k = 2")
151    result2 = solution.rotateGrid([row[:] for row in grid2], 2)
152    print("Output:")
153    for row in result2:
154        print(row)
155    print()
156    
157    # Test case 3: 3x3 matrix (should work but m,n are odd)
158    grid3 = [[1,2,3],[4,5,6],[7,8,9]]
159    print("Input:", grid3)
160    print("k = 1")
161    result3 = solution.rotateGrid([row[:] for row in grid3], 1)
162    print("Output:", result3)