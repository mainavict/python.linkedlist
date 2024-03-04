
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
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode = lastnode.next
            lastnode.next = newnode

    def insert_front(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            firstnode = self.head
            newnode.next = firstnode
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
                break
            if n-j == 1:
                holder = currentnode.next
                currentnode.next = newnode
            if j == n:
                currentnode = newnode
                currentnode.next = holder

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
                break
            if n-j == 1:
                holder = currentnode

            if j == n:
                holder.next = currentnode.next

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
            currentnode = currentnode.next
            j += 1
        held.next = None

    def remove_front_node(self):
        if self.head is None:
            print('The list is empty')
        hold = self.head
        self.head = hold.next

    def mergelist(self, list2):
        lastnode = self.head
        while lastnode is not None:
            if lastnode.next is None:
                lastnode.next = list2.head
                break
            lastnode = lastnode.next


node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node("5")
nodet = Node('0')
linkedlist1 = Linkedlist()
linkedlist1.insert_front(node1)
linkedlist1.insert_front(node2)
linkedlist1.insert_front(node3)
linkedlist1.insert_on_index(node4,0)
# linkedlist1.insert_front(node5)
# linkedlist1.insert_on_index(nodet,0)


#
# linkedlist1.printlist()
#
#
# nodea = Node("a")
# nodeb = Node("b")
# nodec = Node("c")
# noded = Node("d")
# nodee = Node("e")
# nodef = Node("f")
#
#
# linkedlist2 = Linkedlist()
# linkedlist2.insert_end(nodea)
# linkedlist2.insert_end(nodeb)
# linkedlist2.insert_end(nodec)
# linkedlist2.insert_end(noded)
# linkedlist2.insert_end(nodee)
# linkedlist2.insert_end(nodef)
# linkedlist2.printlist()
# linkedlist1.mergelist(linkedlist2)
# linkedlist1.remove_end_node()
linkedlist1.printlist()
print(node1.next)
