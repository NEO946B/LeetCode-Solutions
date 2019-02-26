'''
1. Two Sum
https://leetcode.com/problems/two-sum/
'''

class Solution(object):
    def twoSum(self, nums, target):
        nums_t = {}
        for idx, n in enumerate(nums):
            if n in nums_t:
                return nums_t[n],idx
            nums_t[target-n] = idx
        return 0,0