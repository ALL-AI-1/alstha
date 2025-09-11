
# """Single LInked LIst"""
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class Linked_List:
#     def __init__(self,head=None):
#         self.head=head

#     def insert_at_beginning(self,data):
#         self.head=Node(data,self.head)

#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head=Node(data,None)
#             return
#         itr=self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=Node(data,None)
        
#     def insert_values(self,data_list):
#         for data in data_list:
#             self.insert_at_end(data)
#     def length(self):
#         count=1
#         itr=self.head
#         while itr.next is not None:
#             itr=itr.next
#             count+=1
#         return count


#     def remove_at(self,index):
#         if index<0 or index>=self.length():
#             raise Exception("Invalid_Index")

#         if index==0:
#             self.head=self.head.next
#             return

#         itr=self.head

#         for i in range(self.length()):
#             if i == index-1:
#                 itr.next=(itr.next).next
#             else:
#                 itr=itr.next

#         # count=0
#         # while itr:
#         #     if count==index-1:
#         #         itr.next=itr.next.next
#         #         break
#         #     count+=1
#         #     itr=itr.next

#     def insert_at(self,index,value):
#         if index<0 or index>=self.length():
#             raise Exception("Invalid_Index")

#         if index==0:
#             self.insert_at_beginning(value)
#             return
#         itr=self.head
#         count=0
#         while itr:
#             if count==index-1:
#                 node=Node(value,itr.next)
#                 itr.next=node
#                 break

#             itr=itr.next
#             count+=1

#     def remove_values(self,value):
#         itr=self.head
#         count=0
#         list_of_removing_index=[]
#         while itr:
#             if itr.data==value:
#                 list_of_removing_index.append(count)
            
#             itr=itr.next
#             count+=1
#         for i in sorted(list_of_removing_index,reverse=True):
#             self.remove_at(i)
            
        
#     def insert_after_value(self,insert_after,insert_value):
#         itr=self.head
#         count=0
#         list_of_target_index=[]
#         while itr:
#             if itr.data==insert_after:
#                 list_of_target_index.append(count+1)
            
#             itr=itr.next
#             count+=1
#         for i in sorted(list_of_target_index,reverse=True):
#             self.insert_at(i,insert_value)

                
    
#     def print(self):
#         if self.head is None:
#             print("Linked_List is empty")
#             return
#         itr=self.head
#         itrstr=''
#         while itr:
#             itrstr+=str(itr.data)+ ' --> '
#             itr=itr.next
#         print(itrstr)
    
        
# if __name__=="__main__":
#     ll=Linked_List()
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning("apple")
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning(5)
#     ll.print()

#     ll.insert_at_beginning(52)
#     ll.print()

#     ll.insert_at_end(52)
#     ll.print()

#     ll.insert_values(["apple","banana","orange"])
#     ll.print()

#     ll.remove_at(0)
#     ll.print()

#     ll.remove_at(3)
#     ll.print()

#     ll.insert_at(2,45)
#     ll.print()

#     ll.insert_at(2,9)
#     ll.print()

#     print(ll.length())
#     ll.print()

#     ll.remove_values(5)
#     ll.print()
#     ll.insert_after_value("apple","grapes")
#     ll.print()
    

"""Double Linked List with head and tail"""

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            # If list was empty, new node is also the tail
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        if self.tail is None:
            # List is empty, so insert at beginning
            self.insert_at_beginning(data)
            return
        new_node = Node(data, self.tail, None)
        self.tail.next = new_node
        self.tail = new_node

    def print_forward(self):
        itr = self.head
        dll_str = ''
        while itr:
            dll_str += str(itr.data) + ' <-> '
            itr = itr.next
        print(dll_str.rstrip(' <-> '))

    def print_backward(self):
        itr = self.tail
        dll_str = ''
        while itr:
            dll_str += str(itr.data) + ' <-> '
            itr = itr.prev
        print(dll_str.rstrip(' <-> '))

# Example usage:
if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_end(5)
    dll.insert_at_end(1)
    print("Forward:")
    dll.print_forward()
    print("Backward:")
    dll.print_backward()