class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
    temp = self.head
    if(self.head):
      while(temp.next is not None):
        temp = temp.next
      temp.next = Node(data)
    else:
      self.head = Node(data)
  
  def delete(self, data):
    temp = self.head
    prev = None
    while (temp.data != data and temp.next is not None):
      prev = temp
      temp = temp.next
    
    if temp.next is None:
      return

    prev.next = temp.next
  
  def insert_at_position(self, pos, data):
    temp = self.head
    prev = temp
    count = 0
    if pos == 0:
      self.head = Node(data)
      self.head.next = temp
      return
    while(count < pos and temp.next is not None):
      count += 1
      prev = temp
      temp = temp.next

    prev.next = Node(data)
    prev.next.next = temp

  
  def print_list(self):
    temp = self.head
    while (temp.next is not None):
      print(temp.data)
      temp = temp.next
    print(temp.data)


ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
print('-----before delete------')
ll.print_list()
ll.delete(4)
print('-----after delete------')
ll.print_list()
ll.insert_at_position(0, 4)
print('-----insert at position------')
ll.print_list()