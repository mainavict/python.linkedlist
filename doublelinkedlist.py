
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self, newnode):
        if self.head is None:
            self.head = newnode

        else:
            lastnode = self.head
            if lastnode.next is None:
                newnode.prev = lastnode
            else:
                while lastnode.next is not None:
                    lastnode = lastnode.next
                    if lastnode.next is None:
                        newnode.prev = lastnode
            lastnode.next = newnode

    def insert_front(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            firstnode = self.head
            newnode.next = firstnode
            firstnode.prev = newnode
            self.head = newnode

    def insert_on_index(self, newnode, n):
        if self.head is None and n != 0:
            print("The list is empty")
        j = 0
        currentnode = self.head
        while currentnode:
            if n == 0 and self.head is None:
                self.head = newnode
                break
            if n == 0 and self.head is not None:
                hold = self.head
                self.head = newnode
                self.head.next = hold
                hold.prev = self.head
                break
            if n-j == 1:
                holder = currentnode.next
                currentnode.next = newnode
                newnode.prev = currentnode
                newnode.next = holder
            if j == n:
                hold = currentnode
                currentnode = newnode
                break

            currentnode = currentnode.next
            j += 1

    def printlist(self):
        if self.head is None:
            print("The list is empty")
        currentnode = self.head
        while currentnode:
            print(currentnode.data + '-->', end='')
            currentnode = currentnode.next
        print("\n")

    def printlistindex(self, n):
        if self.head is None:
            print("The list is empty")

        j = 0
        currentnode = self.head
        while currentnode:

            if j == n:
                print(currentnode.data + '-->', end='')
                break

            if currentnode.next is None and j < n:
                print("invalid index")
                break

            currentnode = currentnode.next
            j += 1
        print("\n")

    def removenode(self, n):
        if self.head is None and n != 0:
            print("The list is empty")

        j = 0
        currentnode = self.head
        while currentnode:
            if currentnode.next is None and n > j:
                print('invalid  index')
            if n == 0 and self.head is not None:
                hold = self.head
                self.head = hold.next
                hold1 = hold.next
                hold1.prev = None
                hold.next = None
                break
            if n-j == 1:
                holder = currentnode

            if j == n and currentnode.next is  not None:
                holder.next = currentnode.next
                hold = currentnode.next
                hold.prev = holder
                currentnode.next = None
                currentnode.prev = None
            elif j == n and currentnode.next is None:
                holder.next = currentnode.next
                currentnode.next = None
                currentnode.prev = None




            currentnode = currentnode.next
            j += 1

    def remove_end_node(self):
        if self.head is None:
            print("The list is empty")

        j = 0
        currentnode = self.head
        while currentnode:
            if self.head is not None and self.head.next is None:
                self.head = None
                break
            if currentnode.next is not None:
                held = currentnode
            elif currentnode.next is None:
                currentnode.prev = None
            currentnode = currentnode.next
            j += 1
        held.next = None

    def remove_front_node(self):
        if self.head is None:
            print('The list is empty')
        hold = self.head
        self.head = hold.next
        self.head.prev = None
        hold.next = None

    def mergelist(self, list2):
        if self.head is None or list2.head is None:
            print("Empty list!cant merge an empty list ")
        else:
            lastnode = self.head
            while lastnode is not None:
                if lastnode.next is None:
                    lastnode.next = list2.head
                    list2.head.prev = lastnode
                    break
                lastnode = lastnode.next


