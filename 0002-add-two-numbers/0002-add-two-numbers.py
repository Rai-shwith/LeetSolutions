# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        node = l1
        i = 1
        while node:
            num1+=node.val*i
            i=i*10
            node = node.next
        node = l2
        i = 1
        while node:
            num2+=node.val*i
            i=i*10
            node = node.next
        
        sum = str(num1+num2)
        head = ListNode(int(sum[-1]))
        current = head
        for num in sum[-2::-1]:
            current.next = ListNode(int(num))
            current = current.next
        return head