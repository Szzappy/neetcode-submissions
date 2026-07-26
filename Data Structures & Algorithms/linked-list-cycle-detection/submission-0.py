# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point1 = head
        point2 = head

        while point1 != None or point2 != None:
            try:
                point1 = point1.next
                point2 = (point2.next).next
            except:
                return False

            if point1 == point2:
                return True

        return False