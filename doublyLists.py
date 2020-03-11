'''
This is a Doubly Linked List in python
Functions
- push: adds to front of the list
- print_list: displays list in order and in revesed order
- insert_after: point new node to previous node and the node after the previous with previous pointer and next pointers
'''
import gc
class Node:
    def __init__(self,mobile_number,first_name,last_name):
        self.mobile_number = mobile_number
        self.first_name = first_name
        self.last_name = last_name
        self.prev = prev = None
        self.next = next = None

class Lists:
    def __init__(self):
        self.head = None

    def push(self,mobile_number,first_name,last_name):
        #push new node to front of the list
        new_node = Node(mobile_number,first_name,last_name)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self,prev_node,mobile_number,first_name,last_name):
        if prev_node is None:
            print('No previous node')
            return
        new_node = Node(mobile_number)
        #point next of new_node to the next node of previous
        new_node.next = prev_node.next
        #point previous node to the new node
        prev_node.next = new_node
        #point new node previous to previous node
        new_node.prev = prev_node
        if new_node.next is not None:
            #point the node after the new nodes previous pointer back to the new node
            new_node.next.prev = new_node

    def append(self,mobile_number,first_name,last_name):
        new_node = Node(mobile_number)
        #set the next of the new node to none since it will be the new tail node
        new_node.next = None
        #if list is empty node is the new head
        if self.head is None:
            self.head = new_node

        #get the last node
        find_last = self.head
        while(find_last.next):
            find_last = find_last.next
        #point last node to new node
        find_last.next = new_node
        new_node.prev = find_last

    def search_list(self, data):
        find_data = self.head
        while(find_data):
            if find_data.mobile_number == data:
                print('Contact found: {} {} {}'.format(find_data.first_name,find_data.last_name,find_data.mobile_number))
                return
            find_data = find_data.next
        print('Record not found.')


    def delete_node(self, data):
        find_data = self.head
        #if the node to be deleted is the head
        if self.head.mobile_number == data:
            self.head = find_data.next
            return

        while(find_data):
            if find_data.mobile_number == data:
                print('Contact found: {} {} {}'.format(find_data.first_name,find_data.last_name,find_data.mobile_number))
                #Remove the ndoe that is not the tail
                if find_data.next is not None:
                    find_data.next.prev = find_data.prev
                #change previous if node to be deleted is not the first node
                if find_data.prev is not None:
                    find_data.prev.next = find_data.next
                return
            find_data = find_data.next
        print('Record not found.')


    def print_list(self):
        count = 0
        node = self.head
        while(node):
            count+=1
            print('{} {} {}'.format(node.first_name,node.last_name,node.mobile_number))
            #used to get the last node to print in reversed order
            find_last = node
            node = node.next
        return count
