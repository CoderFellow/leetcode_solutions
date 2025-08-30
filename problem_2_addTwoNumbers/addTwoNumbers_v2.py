class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Solution to the add_two_numbers problem on LeetCode.
        
        args:
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
        
        return:
            dummy_node: node
        """
        dummy_head = ListNode(0)
        current_node = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            carry, sum_value = divmod(val1 + val2 + carry, 10)
        
            current_node.next = ListNode(sum_value)
            current_node = current_node.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy_head.next
