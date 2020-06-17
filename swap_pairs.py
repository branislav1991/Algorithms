class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if not head:
        return None
    if not head.next:
        return head
    
    nextHead = head.next
    def swap(node: ListNode, parent: ListNode):
        if node and node.next:
            nextNode = node.next
            node.next = nextNode.next
            nextNode.next = node
            if parent:
                parent.next = nextNode
            swap(node.next, node)
        
    swap(head, None)
    return nextHead