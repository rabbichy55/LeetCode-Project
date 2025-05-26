list1 = [1,2,4]
list2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode],
                      list2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        point = dummy

        while list1 and list2:
            if list1.val < list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list2.next
            point = point.next

        if list1:
            point.next = list1
        else:
            point.next = list2

        return dummy.next
ss = Solution()
print(ss.mergeTwoLists(list1, list2))