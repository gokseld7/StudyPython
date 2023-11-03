
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        if self.head is None:
            return 0

        currentNode = self.head
        length = 1
        while currentNode.next is not None:
            currentNode = currentNode.next
            length += 1

        return length

    def __str__(self):
        result = ''
        currentNode = self.head
        while currentNode is not None:
            result += str(currentNode.data)
            if currentNode.next is not None:
                result += ' -> '
            currentNode = currentNode.next

        return result

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

    def insertAtIndex(self, index, data):
        if index == 0:
            self.insertAtBeginning(data)
            return

        newNode = Node(data)
        currentNode = self.head
        position = 0
        while currentNode is not None:
            if index == position+1:
                newNode.next = currentNode.next
                currentNode.next = newNode
                return
            currentNode = currentNode.next
            position += 1

        raise IndexError(index)

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtBeginning(data)
            return

        newNode = Node(data)
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = newNode

    def insert(self, data):
        if self.head is None:
            self.insertAtBeginning(data)
            return
        self.insertAtEnd(data)

    def updateNode(self, index, data):
        if self.head is None:
            raise IndexError

        currentNode = self.head
        position = 0
        while currentNode is not None:
            if index == position:
                currentNode.data = data
                return
            currentNode = currentNode.next
            position += 1

        raise IndexError

    def removeFromBeginning(self):
        if self.head is None:
            raise IndexError

        self.head = self.head.next

    def removeFromIndex(self, index):
        if index == 0:
            self.removeFromBeginning()
            return

        currentNode = self.head
        position = 0
        while currentNode is not None:
            if (index == position + 1) and (currentNode.next is not None):
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next
            position += 1

        raise IndexError(index)

    def removeFromEnd(self):
        if self.head is None:
            raise IndexError

        if self.head.next is None:
            self.head = None
            return

        currentNode = self.head
        while currentNode.next.next is not None:
            currentNode = currentNode.next

        currentNode.next = None


if __name__ == '__main__':
    a = LinkedList()
    a.insertAtBeginning('a')
    a.insertAtBeginning('b')
    a.insertAtEnd('e')
    a.insertAtIndex(1, 'x')
    a.updateNode(1, 'c')
    a.insertAtBeginning('hehehe')
    a.insertAtIndex(2, 'general kenobi')
    a.removeFromIndex(4)
    a.removeFromBeginning()
    a.removeFromEnd()
    print(a)

    b = LinkedList()
    b.insert('a')
    b.insert('b')
    b.insert('c')
    b.insert(1)
    b.insert(2)
    b.insert(3)
    print(b)

    c = LinkedList()
    c.insert('x')
    c.removeFromEnd()
    print('c =', c)
