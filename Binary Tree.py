class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            if self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)



root = Node(10)

# Insert more data into the binary tree
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(18)




