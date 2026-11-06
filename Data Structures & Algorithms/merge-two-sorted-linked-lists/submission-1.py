# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head

        list1_pointer = list1
        list2_pointer = list2

        while list1_pointer and list2_pointer:
            if list1_pointer.val <= list2_pointer.val:
                ans.next = list1_pointer
                list1_pointer = list1_pointer.next
            else:
                ans.next = list2_pointer
                list2_pointer = list2_pointer.next
            ans = ans.next
        
        while list1_pointer:
            ans.next = list1_pointer
            list1_pointer = list1_pointer.next
            ans = ans.next
        while list2_pointer:
            ans.next = list2_pointer
            list2_pointer = list2_pointer.next
            ans = ans.next
        return head.next


        