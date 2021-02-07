class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        currentNode = self.head
        counter = 0 
        
        while currentNode:
            if counter == index:
                return currentNode.data
            counter += 1
            currentNode = currentNode.next
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        self.size = self.size + 1
        
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
        
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        currentNode = self.head
        self.size = self.size + 1
        
      
        if not self.head:
            self.head = newNode
        else:
            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.next = newNode
        
        
        
        
   # Node1 --> Node2 --> Node3 --> Node4 --> Node5 --> Node6 --> NULL
   #    index = 3
    #newNode 
    #find Node at Position 3 
    #newNode.next = node3.next
    #node3.next = newNode

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        currentNode = self.head
        
        if index > self.size:
            pass 
        
        elif index == self.size:
            self.addAtTail(val)
            
        else:
            for i in range(index - 1):
                currentNode = currentNode.next
                
            newNode.next = currentNode.next
            currentNode.next = newNode
                
                    
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        currentNode = self.head
        previousNode = None
        
        if index > self.size:
            pass 
        else:
            for i in range(index - 2):
                currentNode = currentNode.next
                
        if currentNode.next:   
            currentNode.next = currentNode.next.next
            self.size = self.size - 1 
                
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Node1 --> Node2 --> Node3 --> Node4 --> Node5 --> Node6 --> NULL 



class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous_node = None
        current_node = head
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
