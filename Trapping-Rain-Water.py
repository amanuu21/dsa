1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        
6        left_max = 0
7        right_max = 0
8        water = 0
9        
10        while left < right:
11            if height[left] < height[right]:
12                if height[left] >= left_max:
13                    left_max = height[left]
14                else:
15                    water += left_max - height[left]
16                left += 1
17            else:
18                if height[right] >= right_max:
19                    right_max = height[right]
20                else:
21                    water += right_max - height[right]
22                right -= 1
23        
24        return water