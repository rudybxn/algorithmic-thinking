class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leftptr = Node(0,0)
        self.rightptr = Node(0,0)
        self.leftptr.next = self.rightptr
        self.rightptr.prev = self.leftptr
        self.leftptr.prev =None
        self.rightptr.next = None
        
    def insert(self,node: Node)->None:
        prv = self.rightptr.prev
        nxt = self.rightptr
        node.prev = prv
        node.next = nxt
        prv.next = node
        nxt.prev = node 

    def remove(self, node: Node)->None:
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insert(newNode)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache)>self.capacity:
                lrunode = self.leftptr.next
                self.remove(lrunode)
                del self.cache[lrunode.key]