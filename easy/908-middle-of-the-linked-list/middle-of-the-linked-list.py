# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         length = 0
#         current = head
#         while current is not None:
#             length += 1
#             current = current.next

#         middle_position = length // 2

#         current = head
#         for i in range(middle_position):
#             current = current.next
        
#         return current

class Solution:
    def middleNode(self, head):
         slow = head
         fast = head
         while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
         return slow