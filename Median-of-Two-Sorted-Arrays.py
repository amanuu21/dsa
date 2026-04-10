1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        # Make sure nums1 is the smaller array
4        if len(nums1) > len(nums2):
5            nums1, nums2 = nums2, nums1
6
7        x, y = len(nums1), len(nums2)
8        low, high = 0, x
9
10        while low <= high:
11            partitionX = (low + high) // 2
12            partitionY = (x + y + 1) // 2 - partitionX
13
14            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
15            minRightX = float('inf') if partitionX == x else nums1[partitionX]
16
17            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
18            minRightY = float('inf') if partitionY == y else nums2[partitionY]
19
20            if maxLeftX <= minRightY and maxLeftY <= minRightX:
21                # Even total length
22                if (x + y) % 2 == 0:
23                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
24                else:
25                    return max(maxLeftX, maxLeftY)
26
27            elif maxLeftX > minRightY:
28                high = partitionX - 1
29            else:
30                low = partitionX + 1