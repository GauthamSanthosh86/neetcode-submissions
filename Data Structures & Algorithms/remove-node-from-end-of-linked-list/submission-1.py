# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#______Brute Force_______

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        #to get where nth point is
        while n > 0 and right:
            right=right.next
            n-=1
        # increments until right reaches null
        while right:
            left=left.next
            right=right.next
        # deletes the nth node
        left.next=left.next.next
        return dummy.next

