class Solution(object):
	def twoSum(self, nums, target):
		"""
		This function checks the indexes of a list
		and sees if they add up to the target, then
		returns those indexes.
	
		args:
			nums: integer list to iterate through.
			target: integer to look for in the list "nums."
	
		returns:
			[]: list of two integers that add up to the "target" variable.
		"""
		# first loop, iterates through nums, as tuples
		for i, k in enumerate(nums):
			
			# iterates with variables i and k with the rest of the list
			for j, l in enumerate(nums):
				if l + k == target and i != j:
					return [i, j]
		
		return [] # returning an empty list if there is no such index's sums equal to target found.


if __name__ == "__main__":
	"""
	main stack block
	"""
	
	# instance of Solution class
	start_operation = Solution()
	
	# lists/arrays and targets
	nums_1 = [2, 7, 11, 15]
	target_1 = 9
	
	nums_2 = [3, 2, 4]
	target_2 = 6
	
	nums_3 = [3, 3]
	target_3 = 6
	
	# ouput
	print(start_operation.twoSum(nums_1, target_1))
