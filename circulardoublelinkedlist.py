
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
            newnode.next = newnode
            newnode.prev = newnode

        else:
            lastnode = self.head
            if lastnode.next is None:
                newnode.prev = lastnode
            else:
                while lastnode.next is not None:
                    if lastnode.next is self.head:
                        newnode.prev = lastnode
                        break
                    lastnode = lastnode.next
            lastnode.next = newnode
            newnode.next = self.head
            self.head.prev = newnode

    def insert_front(self, newnode):
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
        else:
            firstnode = self.head
            newnode.next = firstnode
            newnode.prev = firstnode.prev
            firstnode.prev = newnode
            self.head = newnode
            currentnode = self.head
            while currentnode:
                if currentnode is self.head.prev:
                    currentnode.next = self.head
                    break
                currentnode = currentnode.next

    def insert_on_index(self, newnode, n):
        if self.head is None and n != 0:
            print("The list is empty")
        if n == 0 and self.head is not None:
                hold = self.head
                self.head = newnode
                self.head.next = hold
                self.head.prev = hold.prev
                hold.prev = self.head
                currentnode = self.head
                while  currentnode:
                    if currentnode is self.head.prev:
                        currentnode.next = self.head
                        break
                    currentnode = currentnode.next

        else:
            j = 0
            currentnode = self.head
            while currentnode:
                if n == 0 and self.head is None:
                    self.head = newnode
                    newnode.next = newnode
                    newnode.prev = newnode
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
            if currentnode.next is self.head:
                print(currentnode.data + '-->', end='')
                break
            else:
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

            if currentnode.next is self.head and j < n:
                print("invalid index")
                break

            currentnode = currentnode.next
            j += 1
        print("\n")

    def removenode(self, n):
        if self.head is None :
            print("The list is empty")

        j = 0
        currentnode = self.head
        while currentnode:
            if currentnode.next is self.head and n > j:
                print('invalid  index')
                break
            if n == 0 and self.head.next is self.head:
                self.head = None
                break
            if n == 0 and self.head is not None:
                hold = self.head
                self.head = hold.next
                self.head.prev = hold.prev
                currentnode = self.head
                while currentnode:
                    if currentnode.next is hold:
                        currentnode.next = self.head
                        hold.prev = None
                        hold.next =None
                        break
                    currentnode = currentnode.next
                break
            if n-j == 1:
                holder = currentnode

            if j == n:
                holder.next = currentnode.next
                hold = currentnode.next
                hold.prev = holder
                currentnode.next = None
                currentnode.prev = None
                break
            currentnode = currentnode.next
            j += 1

    def remove_end_node(self):
        if self.head is None:
            print("The list is empty")
        j = 0
        currentnode = self.head
        while currentnode:
            if self.head is not None and self.head.next is self.head:
                self.head = None
                break
            if currentnode.next is not self.head:
                held = currentnode
            if currentnode.next is self.head:
                currentnode.next = None
                currentnode.prev = None
                break
            currentnode = currentnode.next
            j += 1
        held.next = self.head
        self.head.prev = held

    def remove_front_node(self):
        if self.head is None:
            print('The list is empty')
        else:
            hold = self.head
            self.head = hold.next
            self.head.prev = hold.prev
            currentnode = self.head
            while currentnode:
                if currentnode.next is hold:
                    currentnode.next = self.head
                    hold.prev =None
                    hold.next = None
                    break
                currentnode = currentnode.next

    def mergelist(self, list2):
        if self.head is None or list2.head is None:
            print("Empty list ,cant merge an empty list ")
        # elif list2.head is None:
        #     print(f"{list2} is an empty list ,cant merge an empty list")
        else:
            lastnode = self.head.next
            while lastnode is not None:
                if lastnode.next is  self.head:
                    lastnode.next = list2.head
                    list2.head.prev = lastnode
                    break
                lastnode = lastnode.next

                lastnode1 = list2.head
            while  lastnode1:
                if lastnode1.next is list2.head:
                    lastnode1.next = self.head
                    self.head.prev = lastnode1
                    break
                lastnode1 = lastnode1.next

