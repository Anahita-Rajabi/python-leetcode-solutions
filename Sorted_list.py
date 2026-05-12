class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        current = dummy

        # compare both linked lists
        while list1 and list2:

            # take smaller value
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # remaining nodes
        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next