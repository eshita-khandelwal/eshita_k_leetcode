"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a hashmap that will store all the new nodes created. the new nodes will have exact same val of the given nodes in the linked list. 
        hashmap={None:None}
        cur =head
        while cur:
            copy = Node(cur.val)
            hashmap[cur]=copy
            cur = cur.next
        
        cur = head
        while cur:
            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur=cur.next
        return hashmap[head]