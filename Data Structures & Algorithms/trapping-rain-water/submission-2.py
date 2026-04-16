from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0  # final answer

        # loop over every index (each bar)
        for i in range(n):

            # -------------------------
            # 1. Find maximum on LEFT
            # -------------------------
            leftMax = 0
            for j in range(i, -1, -1):   # go from i → 0
                leftMax = max(leftMax, height[j])

            # -------------------------
            # 2. Find maximum on RIGHT
            # -------------------------
            rightMax = 0
            for j in range(i, n):        # go from i → n-1
                rightMax = max(rightMax, height[j])

            # -------------------------
            # 3. Water stored at index i
            # -------------------------
            water_at_i = min(leftMax, rightMax) - height[i]

            # only add if positive
            if water_at_i > 0:
                total_water += water_at_i

        return total_water