1from collections import defaultdict, deque
2from math import isqrt
3from typing import List
4
5class Solution:
6    def minJumps(self, nums: List[int]) -> int:
7        n = len(nums)
8        if n == 1:
9            return 0
10        
11        # Find all primes up to max(nums)
12        max_val = max(nums)
13        is_prime = self.sieve_of_eratosthenes(max_val)
14        
15        # Group indices by prime factors of their values
16        # This mapping will help us quickly find all indices with numbers divisible by a given prime
17        numbers_by_prime = defaultdict(list)
18        for i, val in enumerate(nums):
19            for prime in self.get_prime_factors(val, is_prime):
20                numbers_by_prime[prime].append(i)
21        
22        # BFS
23        visited_index = set()
24        visited_prime = set()
25        queue = deque()
26        queue.append((0, 0))  # (index, distance)
27        visited_index.add(0)
28        
29        while queue:
30            idx, dist = queue.popleft()
31            
32            if idx == n - 1:
33                return dist
34            
35            # 1. Adjacent moves
36            for next_idx in [idx - 1, idx + 1]:
37                if 0 <= next_idx < n and next_idx not in visited_index:
38                    visited_index.add(next_idx)
39                    queue.append((next_idx, dist + 1))
40            
41            # 2. Prime teleportation
42            val = nums[idx]
43            if val > 1 and is_prime[val]:
44                prime = val
45                if prime not in visited_prime:
46                    visited_prime.add(prime)
47                    # Jump to all indices where nums[j] is divisible by this prime
48                    for next_idx in numbers_by_prime[prime]:
49                        if next_idx != idx and next_idx not in visited_index:
50                            visited_index.add(next_idx)
51                            queue.append((next_idx, dist + 1))
52        
53        return -1  # No path found
54    
55    def sieve_of_eratosthenes(self, n: int) -> List[bool]:
56        """Return boolean array where True indicates prime numbers up to n"""
57        if n < 2:
58            return [False] * (n + 1)
59        is_prime = [True] * (n + 1)
60        is_prime[0] = is_prime[1] = False
61        for i in range(2, isqrt(n) + 1):
62            if is_prime[i]:
63                for j in range(i * i, n + 1, i):
64                    is_prime[j] = False
65        return is_prime
66    
67    def get_prime_factors(self, n: int, is_prime: List[bool]) -> set:
68        """Return set of prime factors of n"""
69        if n <= 1:
70            return set()
71        
72        factors = set()
73        
74        # Handle factor 2 separately
75        if n % 2 == 0:
76            factors.add(2)
77            while n % 2 == 0:
78                n //= 2
79        
80        # Check odd factors up to sqrt(n)
81        for i in range(3, isqrt(n) + 1, 2):
82            if n % i == 0:
83                if is_prime[i]:
84                    factors.add(i)
85                while n % i == 0:
86                    n //= i
87        
88        # If remaining n is prime and > 1
89        if n > 1 and is_prime[n]:
90            factors.add(n)
91        
92        return factors