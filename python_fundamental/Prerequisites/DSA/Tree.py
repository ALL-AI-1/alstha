



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.parent=None
#         self.children=[]

#     def add_child(self,child):
#         child.parent=self
#         self.children.append(child)

#     def printt(self):

#         indentation="  "*self.level()

#         print(indentation+self.data)
#         if self.children:
#             for child in self.children:
#                 child.printt()

#     def level(self):
#         level=0
#         p=self.parent

#         while p:
#             level+=1
#             p=p.parent
#         return level

# if __name__=="__main__":
#     School=Node("School")
#     Teacher=Node("Teacher")

#     Teacher.add_child(Node("ta"))
#     Teacher.add_child(Node("tb"))
#     Teacher.add_child(Node("tc"))

#     Student=Node("Student") 

#     Student.add_child(Node("sa"))
#     Student.add_child(Node("sb"))
#     Student.add_child(Node("sc"))

#     Administrator=Node("Administrator")
    
#     Administrator.add_child(Node("aa"))
#     Administrator.add_child(Node("ab"))
#     Administrator.add_child(Node("ac"))

#     School.add_child(Teacher)
#     School.add_child(Student)
#     School.add_child(Administrator)

#     School.printt() 

#     # Traversal
#     #     1 In -Order
#     #     2 Pre-Order
#     #     3 Post-Order
#     # Order
#     #     1 Left -i Node Right
#     #     2 Node -i Left Right
#     #     3 Left -i Right Node
#     # Key Use Case
#     #     1 Sorted data, expression parsing
#     #     2 Serialization, Ul rendering
#     #     3 Cleanup, evaluation, dependency solving

# class BinarySearchTreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

#     def add_child(self,data):
#         if data==self.data:
#             return

#         if data<self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left=BinarySearchTreeNode(data)

#         if data>self.data:
#             if self.right:
#                 self.right.add_child(data)

#             else:
#                 self.right=BinarySearchTreeNode(data)

#     def in_order_traversal(self):
#         element=[]

#         if self.left:
#             element+= self.left.in_order_traversal()

#         element.append(self.data)

#         if self.right:
#             element+= self.right.in_order_traversal()

#         return element

#     def find_min(self):
        
#         if self.left:
#             self.left.find_min()
#         return self.data

# def build_tree(element):
#     root=BinarySearchTreeNode(element[2])

#     for i in range(1,len(element)):
#         root.add_child(element[i])

#     return root

# if __name__=="__main__":
#     numbers=[12,3,22,3,2,44,30,7,88,65,34,11,32]
#     tree=build_tree(numbers)
#     print(tree.in_order_traversal())
#     print(tree.in_order_traversal())
#     print(tree.find_min())

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.value:
            return  # Value already exists
        
        if data < self.value:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:  # data > self.value
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.value
        return self.right.find_max()

    def calculate_sum(self):
        sum_value = self.value
        if self.left:
            sum_value += self.left.calculate_sum()
        if self.right:
            sum_value += self.right.calculate_sum()
        return sum_value

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.value)
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.value)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def search(self,targett):
        if targett==self.value:
            return True
        if targett<self.value and self.left:
            return self.left.search(targett)
        if targett>self.value and self.right:
            return self.right.search(targett)
        return False

def build_tree(elements):
    if not elements:
        return None
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    numbers = [12, 3, 22, 3, 2, 44, 30, 7, 88, 65, 34, 11, 32]
    tree = build_tree(numbers)
    print("In-order traversal:", tree.in_order_traversal())
    print("Pre-order traversal:", tree.pre_order_traversal())
    print("Post-order traversal:", tree.post_order_traversal())
    print("Minimum value:", tree.find_min())
    print("Maximum value:", tree.find_max())
    print("Sum of all values:", tree.calculate_sum())
    print("Search value:", tree.search(88))
    print("Search value:", tree.search(8))
