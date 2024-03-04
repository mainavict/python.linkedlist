
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self, newnode):
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
        else:
            lastnode = self.head
            while lastnode.next :
                if lastnode.next is self.head:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newnode
            newnode.next = self.head

    def insert_front(self, newnode):
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            lastnode = self.head
            while lastnode.next :
                if lastnode.next is self.head:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newnode
            firstnode = self.head
            newnode.next = firstnode
            self.head = newnode
    def insert_on_index(self, newnode, n):
        # if self.head is None and n != 0:
        #     print("The list is empty")
        j = 0
        currentnode = self.head
        saver = self.head

        if n == 0 and self.head is not None:
            h1 = self.head
            self.head = newnode
            self.head.next = h1
            leve = h1
            while leve.next is not h1:
                leve = leve.next
            leve.next = self.head
        else:
            if n == 0 and self.head is None:
                    self.head = newnode
                    newnode.next = self.head

            else:
                while currentnode:

                    if n-j == 1:
                        holder = currentnode.next
                        currentnode.next = newnode
                    if j == n:
                        currentnode = newnode
                        currentnode.next = holder
                    if currentnode.next is  saver:
                      break
                    else:
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
        saver = self.head
        while currentnode:
            if currentnode.next is None and n > j:
                print('invalid  index')
            if n == 0 and self.head is not None:
                hold = self.head
                self.head = hold.next
                swap = hold
                while swap.next is not  hold:
                    swap = swap.next
                swap.next = self.head
                break
            if n-j == 1:
                holder = currentnode

            if j == n:
                holder.next = currentnode.next

            if currentnode.next is  saver:
                  break
            else:
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
            elif currentnode.next is self.head:
                break
            currentnode = currentnode.next
            j += 1



        held.next = self.head

    def remove_front_node(self):
        if self.head is None:
            print('The list is empty')
        hold = self.head
        self.head = hold.next
        currentnode = self.head
        while currentnode.next is not hold:
            currentnode = currentnode.next
        currentnode.next = self.head

    def mergelist(self, list2):
        lastnode = self.head
        while lastnode.next :
            if lastnode.next is self.head:
                lastnode.next = list2.head
                break
            lastnode = lastnode.next

        lastnode2 = list2.head
        while lastnode2:
            if lastnode2.next is list2.head:
                lastnode2.next = self.head
                break
 
