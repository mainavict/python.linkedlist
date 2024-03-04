insert_end(self, newnode) - inserts  a node in a list on last index,if there are no nodes in the list the node will be inserted  as te head of the list.
                            NB:newnode in (insert_end(self, newnode)) is the node u want to insert

insert_front(self, newnode)  - inserts on the index zero node ,if the list was empty it makes the node the head of the list
                               NB:newnode in (insert_end(self, newnode)) is the node u want to insert

insert_on_index(self, newnode, n) - inserts the  node on a specific index of the node ,if the index given (n) is more the  indexs in the list it will give a message  invalide index
                                     NB:newnode in (insert_end(self, newnode)) is the node u want to insert and the (n) is the index,indexing starts at 0.

printlist(self) -  prints  the node.data in the list,if the list is empty it will print ''The list is empty'

printlistindex(self, n) - prints  the node.data on a specified index in a list,if lit is empty it will print 'the list is empty'
                          NB: (n) in printlistindex(self, n) is an integer parameter to indicate the index u specify

removenode(self, n) -removes a specified node on he list ,if the list is empty  it will print the list is empty
                    NB:(n) in  removenode(self, n) is an integer parameter  to indicate the index u wamt to remove,indexing starts at 0

remove_front_node(self) - it removes the node at index zero

 remove_end_node(self) =it removes the last node on the list

 mergelist(self, list2) - it joins two lists.to one list
                          NB:list2 in  (mergelist(self, list2)) is the list u want to join with 



sample code:
1:
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node("5")
nodet = Node('0')

linkedlist1 =Linkedlist()
linkedlist1.insert_front(node1)
linkedlist1.insert_end(node2)
linkedlist1.printlist()
print(node2.next.data)
print("end of list 1")

results:
1-->2-->

1
end of list 1


2:
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node("5")
nodet = Node('0')

linkedlist1 =Linkedlist()
linkedlist1.insert_front(node1)
linkedlist1.insert_end(node2)
linkedlist1.printlist()
print(node2.next.data)
print("end of list 1")

linkedlist2 = Linkedlist()
linkedlist2.insert_front(node3)
linkedlist2.insert_end(node4)
linkedlist2.insert_end(node5)
linkedlist2.printlist()
print(node5.next.data)
print("end of list2\n")

result:

1-->2-->

1
end of list 1
3-->4-->5-->

3
end of list2



3:
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node("5")
nodet = Node('0')

linkedlist1 =Linkedlist()
linkedlist1.insert_front(node1)
linkedlist1.insert_end(node2)
linkedlist1.printlist()
print(node2.next.data)
print("end of list 1")

linkedlist2 = Linkedlist()
linkedlist2.insert_front(node3)
linkedlist2.insert_end(node4)
linkedlist2.insert_end(node5)
linkedlist2.printlist()
print(node5.next.data)
print("end of list2\n")

linkedlist1.mergelist(linkedlist2)
linkedlist1.insert_on_index(nodet,0)
linkedlist1.printlist()
print(node5.next.data)
print("this is the merged list 1 and 2")

results:
1-->2-->

1
end of list 1
3-->4-->5-->

3
end of list2

0-->1-->2-->3-->4-->5-->

0
this is the merged list 1 and 2

4:
nodea = Node("a")
nodeb = Node("b")
nodec = Node("c")
noded = Node("d")
nodee = Node("e")
nodef = Node("f")
linkedlist3 = Linkedlist()
linkedlist3.insert_front(nodea)
linkedlist3.insert_end(nodeb)
linkedlist3.insert_end(nodec)
linkedlist3.insert_end(noded)
linkedlist3.insert_end(nodee)
linkedlist3.insert_end(nodef)

linkedlist3.printlist()
print(nodef.next.data)

linkedlist3.mergelist(linkedlist1)
linkedlist3.remove_end_node()
linkedlist3.printlist()
print(node4.next.data)
results:
a-->b-->c-->d-->e-->f-->

a
a-->b-->c-->d-->e-->f-->0-->1-->2-->3-->4-->

a


