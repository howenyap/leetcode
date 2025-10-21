from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        res = 0
        
        while prev:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return res


        
