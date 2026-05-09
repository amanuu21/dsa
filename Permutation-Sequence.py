1class Solution:
2    def getPermutation(self, n: int, k: int) -> str:
3        # Convert to 0-based index for easier calculation
4        k -= 1
5        
6        # Create list of numbers 1..n
7        numbers = list(range(1, n + 1))
8        
9        # Precompute factorials
10        factorial = [1] * n
11        for i in range(1, n):
12            factorial[i] = factorial[i - 1] * i
13        
14        result = []
15        
16        # Build the permutation digit by digit
17        for i in range(n, 0, -1):
18            # Number of permutations starting with each remaining digit
19            block_size = factorial[i - 1]
20            
21            # Determine which digit belongs at this position
22            index = k // block_size
23            
24            # Add the chosen digit to result
25            result.append(str(numbers[index]))
26            
27            # Remove the used digit
28            numbers.pop(index)
29            
30            # Update k for the remaining positions
31            k %= block_size
32        
33        return ''.join(result)
34
35
36# Alternative implementation with clearer comments
37class SolutionDetailed:
38    def getPermutation(self, n: int, k: int) -> str:
39        """
40        Finds the kth permutation of [1, 2, ..., n] in lexicographic order.
41        
42        Args:
43            n: The range 1..n
44            k: The kth permutation (1-indexed)
45        
46        Returns:
47            The kth permutation as a string
48        """
49        # Calculate factorials: fact[i] = i!
50        fact = [1] * (n + 1)
51        for i in range(2, n + 1):
52            fact[i] = fact[i - 1] * i
53        
54        # List of available numbers
55        nums = list(range(1, n + 1))
56        
57        # Convert k to 0-indexed
58        k -= 1
59        
60        result = []
61        
62        # Build the permutation
63        for i in range(n, 0, -1):
64            # There are (i-1)! permutations starting with each digit
65            # Find which block our k falls into
66            block_size = fact[i - 1]
67            index = k // block_size
68            
69            # Append the chosen number
70            result.append(str(nums[index]))
71            
72            # Remove used number
73            nums.pop(index)
74            
75            # Update k for remaining positions
76            k %= block_size
77        
78        return ''.join(result)
79
80
81# Example usage
82if __name__ == "__main__":
83    solution = Solution()
84    
85    # Test case 1: n = 3, k = 3
86    print(f"n=3, k=3: {solution.getPermutation(3, 3)}")  # Output: "213"
87    
88    # Test case 2: n = 4, k = 9
89    print(f"n=4, k=9: {solution.getPermutation(4, 9)}")  # Output: "2314"
90    
91    # Test case 3: n = 3, k = 1
92    print(f"n=3, k=1: {solution.getPermutation(3, 1)}")  # Output: "123"
93    
94    # Test case 4: n = 3, k = 6
95    print(f"n=3, k=6: {solution.getPermutation(3, 6)}")  # Output: "321"
96    
97    # Test case 5: n = 4, k = 24 (last permutation)
98    print(f"n=4, k=24: {solution.getPermutation(4, 24)}")  # Output: "4321"