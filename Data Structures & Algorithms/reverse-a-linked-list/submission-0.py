# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = head

        returnVal = None

        if index == None:
            return index

        while index.next != None:
            temp = ListNode(index.val, index.next)
            temp.next = returnVal
            returnVal = temp

            index = index.next

        index.next = returnVal

        return index