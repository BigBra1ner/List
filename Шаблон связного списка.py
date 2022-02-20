
class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_end(self, value=None):
        """

        """
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.nextNode = newNode
        self.tail = self.tail.nextNode

    def lenLinkedList(self):#Длина списка
        if self.head is None:
            return 0
        else:
            n = 1
            lastNode = self.head
            while lastNode.nextNode:
                lastNode = lastNode.nextNode
                n += 1
            return n


    def find_by_value(self, v):
        if self.head is None:
            return -1
        else:
            n = 0
            lastNode = self.head
            while lastNode.nextNode:
                if lastNode.value == v:
                        return n
                else:
                    n += 1
                    lastNode = lastNode.nextNode
            if lastNode.value == v:
                return n
            else:
                return -1

    def find_by_index(self, index):
        if self.head is None:
            return None
        else:
            n = 0
            lastNode = self.head
            while lastNode.nextNode:
                if n == index:
                    return lastNode.value
                else:
                    n += 1
                    lastNode = lastNode.nextNode
            if n == index:
                return lastNode.value
            else:
                return None

    def del_head(self):
        lastNode = self.head
        self.head = lastNode.nextNode

    def print(self):
        if self.head is None:
            return

        node = self.head
        while node is not None:
            print(node.value)
            node = node.nextNode

    def del_element(self, v):
        if self.head is None:
            return
        if self.head.value == v:
            LinkedList.del_head(self)
            return
        currNode = self.head
        prevNode = None
        while currNode is not None:
            if currNode.value == v:
                    prevNode.nextNode = currNode.nextNode
                    return
            prevNode = currNode
            currNode = currNode.nextNode


    def change_list(self):
        prevNode = None
        currNode = self.head
        nextNo = None
        while currNode is not None:
            nextNo = currNode.nextNode
            currNode.nextNode = prevNode
            prevNode = currNode
            currNode = nextNo
        self.head = prevNode
        return

    def add_index(self, n, value=None):
        b = mylist.lenLinkedList() - 1
        if n > b + 1:
            return
        else:
            NewNode = Node(value)
            if n == 0:
                NewNode.nextNode = self.head
                self.head = NewNode
                return
            if n == b + 1:
                self.tail.nextNode = NewNode
                self.tail = self.tail.nextNode
                return
            else:
                index = 0
                lastNode = self.head
                while lastNode.nextNode:
                    if index == n - 1:
                        NewNode.nextNode = lastNode.nextNode
                        lastNode.nextNode = NewNode
                        return
                    else:
                        index += 1
                        lastNode = lastNode.nextNode
                return
if __name__ == "__main__":

    mylist = LinkedList()
    mylist.add_to_end("Why?")
    mylist.add_to_end("Where?")
    mylist.add_to_end("What?")
    mylist.add_to_end("?")
    mylist.add_to_end("Which?")
    mylist.change_list()
    mylist.print()
