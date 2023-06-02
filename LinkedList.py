"""
@author: ansh997
Simple implementation of LinkedList and Circular Linked List in python.


/*     ---------    ---------           */
/*     | Value |    | Value |           */
/*     |  ---  |    |  ---  |           */
/*     |  next-|--> |  next-|----       */
/*     ---------    ---------   |       */
/*     |                        |       */
/*     -------------------------        */
"""


class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = self


class CLL:

  def __init__(self):
    self.head = None
    self.count = 0

  def __repr__(self):
    string = ""
    if self.head == None:
      string += "Circular Linked List Empty"
      return string

    string += f"Circular LinkedList:\n{self.head.data}"
    temp = self.head.next
    while (temp != self.head):
      string += f" -> {temp.data}"
      temp = temp.next
    return string

  def append(self, data):
    self.insert(data, self.count)
    return

  def insert(self, data, index):
    if (index > self.count) | (index < 0):
      raise ValueError(f"Index out of range: {index}, size: {self.count}")
    if self.head == None:
      # Instantiating a CLL.
      self.head = Node(data)
      self.count += 1
      return
    temp = self.head
    for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
      temp = temp.next

    aftertemp = temp.next  # new node goes between temp and after temp
    temp.next = Node(data)
    temp.next.next = aftertemp
    if (index == 0):
      self.head = temp.next
    self.count += 1
    return

  def remove(self, index):
    if (index >= self.count) | (index < 0):
      raise ValueError(f"Index out of range: {index}, size: {self.count}")
    if self.count == 1:
      self.head = None
      self.count = 0
      return
    before = self.head
    for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
      before = before.next
    after = before.next.next
    before.next = after
    if (index == 0):
      self.head = after
    self.count -= 1
    return

  def index(self, data):
    temp = self.head
    for i in range(self.count):
      if (temp.data == data):
        return i
      temp = temp.next
    return None

  def size(self):
    return self.count

  def display(self):
    print(self)


if __name__ == '__main__':
  ll_nums = CLL()
  print(ll_nums)

  ll_nums.append(1)
  ll_nums.append(2)
  ll_nums.append(3)
  ll_nums.append(4)
  ll_nums.append(5)

  print(ll_nums)
  # Check Below that this is a CLL.
  cnt = 0
  temp = ll_nums.head
  while (temp):
    brk = ' '
    cnt += 1
    if (cnt == 25):
      break
    if cnt % 5 == 0:
      brk = '\n'
    print(temp.data, end=brk)
    temp = temp.next
