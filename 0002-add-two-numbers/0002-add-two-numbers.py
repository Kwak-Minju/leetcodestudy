# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
 
        first= ""
        second = ""

        while l1:
            first = str(l1.val) +first
            l1=l1.next
        while l2:
            second = str(l2.val) +second
            l2=l2.next

        sTotal = str(int(first)+int(second))
        print(f"sTotal : {sTotal}")

        head = None
        for i in sTotal:
            node = ListNode(val=i,next=head)
            print(f"val-{node.val} / next-{node.next}")
            head = node

        return head
        