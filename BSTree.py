from node import Node
class Tree:
    def __init__(self):
        self.root = None
        print("initializing bstree")

    def printInorder(self):

        def inorderHelper(root):
            if not root:
                return
            inorderHelper(root.left)
            print(root.data,end=' ')
            inorderHelper(root.right)
        inorderHelper(self.root)


    def insert(self, data):

        def insertHelper(root,data):
            if not root:
                newNode = Node.Node(data)
                root = newNode
            elif data <= root.data:
                root.left = insertHelper(root.left,data)
            else:
                root.right = insertHelper(root.right, data)
            return root
        self.root = insertHelper(self.root,data)


