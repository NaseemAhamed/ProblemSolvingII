class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sum_of_linked_lists(self, l1, l2):
        a = l1
        b = l2
        c = 0
        ret = current = None
        while a or b:
            val = a.val + b.val + c
            c = val // 10

            if not current:
                ret = current = Node(val % 10)
            else:
                current.next = Node(val % 10)
                current = current.next

            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            elif c:
                current.next = c

            a = a.next
            b = b.next
        return ret


l1 = Node(3)
l1.next = Node(4)
l1.next.next = Node(2)
l2 = Node(7)
l2.next = Node(5)
l2.next.next = Node(5)

answer = Solution().sum_of_linked_lists(l1, l2)
while answer:
    print(answer.val, ' ')
    answer = answer.next
