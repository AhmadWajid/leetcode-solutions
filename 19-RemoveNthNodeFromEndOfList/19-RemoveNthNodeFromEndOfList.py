# Last updated: 11/26/2025, 8:55:40 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ahead = dummy
        slow = dummy
        for i in range(n+1):
            ahead = ahead.next
        while ahead:
            ahead = ahead.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next