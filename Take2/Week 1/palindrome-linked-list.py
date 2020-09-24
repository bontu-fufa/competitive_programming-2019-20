#https://leetcode.com/problems/palindrome-linked-list
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        def reverse(head):
            prev = None
            current = head
            if current is None:
                return
            nxt = current.next
            while nxt:
                current.next = prev
                prev = current
                current = nxt
                nxt = nxt.next
            current.next = prev
            return current
        
        #get lenght and mid
        length = 0
        h = head
        while h:
            length += 1
            h = h.next
        if length == 1 : return True
        mid = length // 2
        if length % 2 != 0 :
            mid += 1

        # get mid element
        cur = head
        for i in range(mid):
            print(cur.val,cur.next.val)
            cur = cur.next

        # reverse
        cur = reverse(cur)
        
        # similarity check
        while head and cur: 
            if head.val != cur.val :
                return False
            head,cur = head.next,cur.next  
        return True
