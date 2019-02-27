'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/submissions/

@author: neo.huang3@gmail.com
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l,r = 0,len(height)-1
        while l < r:
            h_l, h_r = height[l], height[r]
            if h_l < h_r:
                area = h_l * (r - l)
                while height[l] <= h_l:
                    l += 1
            else:
                area = h_r * (r - l)
                while height[r] <= h_r and r:
                    r -= 1
            if area > max_area:
                max_area = area
        return max_area