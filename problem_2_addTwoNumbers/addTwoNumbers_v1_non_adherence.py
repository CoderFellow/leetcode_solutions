# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		This function adds the lists correctly, however does not
		adhere to the leetcode specs. It didn't use l1 and l2 as list
		nodes.
		
		args:
			l1: ListNode
			l2: ListNode
			
		return:
			new_list: integer list
		"""
		# important variables
		l3 = []
		l1_reversed_figure = 0
		l2_reversed_figure = 0
		converter_a = 1
		converter_b = 1

		# converting l1 into a whole number
		for l1_element in l1:
			temp_fig = converter_a * l1_element
			l1_reversed_figure += temp_fig
			converter_a *= 10
			
		# converting l2 into a whole number
		for l2_element in l2:
			temp_fig = converter_b * l2_element
			l2_reversed_figure += temp_fig
			converter_b *= 10
		
		# adding l1 and l2 as whole numbers
		new_fig = l1_reversed_figure + l2_reversed_figure
		
		# putting the sum of l1 and l2 in a list
		l3 = [int(digit) for digit in str(new_fig)]
		
		# reversing the list of the sum of l1 and l2
		l3.reverse()
		
		# returning new_list
		return l3


if __name__ == "__main__":        
	"""
	main function
	"""
	start_function = Solution()
	
	l1 = [1, 2, 3, 5]
	l2 = [4, 5, 6]
	# expected ouput
	#  = [5, 7, 9, 5]

x = start_function.addTwoNumbers(l1, l2)
print(x)
