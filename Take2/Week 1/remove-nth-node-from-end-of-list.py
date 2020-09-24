#https://leetcode.com/problems/remove-nth-node-from-end-of-list

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    pointer  = head
    length = 0

    while pointer :
        length += 1
        pointer = pointer.next

    length = length - n

    cur = head
    prev = None
    while length > 0:

        prev = cur
        cur = cur.next
        length -= 1
    if not prev :
        return head.next

    prev.next = cur.next
    return head 
