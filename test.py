#step1: define a node

class Node:
    def __init__(self,data):
        self.data=data# The value is saved in the node
        self.next=None# points to the next node. the default is none

#step2: define linkedlist()
class LinkedList:
    def __init__(self):
        self.head=None# start with an empty list
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:#IF LIST IS EMPTY
            self.head=new_node# now new node becomes the head
        else:
            current=self.head
            while current.next:# move to the end
                current=current.next
            current.next=new_node#link the last node to new node

    #method to print the list    
    def print_list(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")

#use the linked list
my_list=LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

#output the list
my_list.print_list()





