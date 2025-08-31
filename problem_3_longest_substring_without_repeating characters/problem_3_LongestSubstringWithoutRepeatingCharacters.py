class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# maximum length variable initialized to 0.
		maximum_length = 0
		char_index_map = {}
		start = 0
		end = 0
		
		# checking if character is in dictionary
		# and if it's last seen index is within the current window.
		for end, character in enumerate(s):
			if character in char_index_map and char_index_map[character] >= start:
				start = char_index_map[character] + 1
			
			# storing th character's current index in dictionary
			char_index_map[character] = end
			
			# updating max length
			maximum_length = max(maximum_length, end - start + 1)
			
		# returning max length
		return maximum_length
