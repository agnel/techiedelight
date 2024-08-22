# Find a pair with the given sum in an array
# Ref: https://www.techiedelight.com/find-pair-with-given-sum-array/
# tags: array, hash, dictionary
'''

Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

'''
from collections import defaultdict

class Solution:
	def findPair(self, nums: List[int], target: int) -> Tuple[int]:
		
		# Write your code here...
		
		d = defaultdict(int)
		
		for i, n in enumerate(nums):
			if target - n in d:
				return (nums[d[target - n]], nums[i])
			
			d[n] = i
		
		
		return ()

