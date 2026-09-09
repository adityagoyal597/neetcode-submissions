class Node:

    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def removeNode(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    # inserting before the Right node , making it the MRU
    def insertNode(self,node):
        prev=self.right.prev
        next=self.right

        prev.next=node
        next.prev=node

        node.next=next
        node.prev=prev
        

    def get(self, key: int) -> int:

        if key in self.cache:
            self.removeNode(self.cache[key])
            # making it MRU
            self.insertNode(self.cache[key])
            return self.cache[key].val
        # if doesn't exist
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # removing the old value of the node 
            self.removeNode(self.cache[key])
        #creatingthe newNode
        self.cache[key]=Node(key,value)
        self.insertNode(self.cache[key])
        
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]