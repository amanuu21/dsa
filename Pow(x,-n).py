1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        # Base case: any number to the power of 0 is 1
4        if n == 0:
5            return 1.0
6        
7        # Handle negative exponents
8        if n < 0:
9            x = 1 / x
10            n = -n
11        
12        result = 1.0
13        current_product = x
14        
15        # Binary exponentiation
16        while n > 0:
17            # If current bit is 1, multiply result by current_product
18            if n & 1:
19                result *= current_product
20            
21            # Square the base for the next bit
22            current_product *= current_product
23            
24            # Shift right to process next bit
25            n >>= 1
26        
27        return result
28
29
30# Alternative recursive implementation (more intuitive but uses recursion)
31class SolutionRecursive:
32    def myPow(self, x: float, n: int) -> float:
33        if n == 0:
34            return 1.0
35        
36        if n < 0:
37            return 1 / self.myPow(x, -n)
38        
39        # If n is even: x^n = (x^(n/2))^2
40        if n % 2 == 0:
41            half = self.myPow(x, n // 2)
42            return half * half
43        # If n is odd: x^n = x * x^(n-1)
44        else:
45            return x * self.myPow(x, n - 1)
46
47
48# Test cases
49if __name__ == "__main__":
50    solution = Solution()
51    
52    # Test cases
53    print(solution.myPow(2.000, 10))   # 1024.0
54    print(solution.myPow(2.100, 3))    # 9.261
55    print(solution.myPow(2.000, -2))   # 0.25
56    print(solution.myPow(0.000, 5))    # 0.0
57    print(solution.myPow(1.000, 1000)) # 1.0
58    print(solution.myPow(2.000, 0))    # 1.0
59    print(solution.myPow(0.001, 3))    # 1e-09