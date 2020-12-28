#
from typing import Any, List


class Node:
    """Node class to create node in linked list
    """
    def __init__(self, data: int) -> None:
        self.data:int = data
        self.next: Any = None

class LinkedList:
    """This class is for creating linked list by linked nodes
    """
    
    def __init__(self) -> None:
        self.head = None
    
    def add_elements(self):
        pass
    
    def insert(self, pos, data):
        pass

    def get(self, data):
        pass

    def delete(self, pos):
        temp_ptr = self.head
        prev_ptr = self.head
        i: int = 0
        while(temp_ptr != None):
            if i ==  pos:
                prev_ptr.next = temp_ptr.next
            if i != pos-1:
                prev_ptr = prev_ptr.next
            temp_ptr = temp_ptr.next
            i += 1

    def print_list(self):
        if not self.head:
            return None
        temp_ptr = self.head
        while(temp_ptr!= None):
            print(temp_ptr.data, '->')
            temp_ptr = temp_ptr.next


if __name__ == '__main__':

    data: List[int] = [1,2,31,2,3,2,31,2]
    llist = LinkedList()
    i: int = 1
    llist.head = Node(data[0])
    head_ptr = llist.head
    while(len(data) > i):
        node = Node(data[i])
        head_ptr.next = node
        head_ptr = node
        i += 1
    llist.print_list()
    # llist.delete(2)
    # llist.delete(1)
    # llist.delete(4)
    # llist.print_list()
