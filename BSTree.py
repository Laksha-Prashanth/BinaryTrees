from node import Node
class Tree:
    def __init__(self):
        self.root = None
        self.levels = 0

    def print_inorder(self):
        self.__inorderHelper(self.root)

    def __inorderHelper(self,root):
        if not root:
            return
        self.__inorderHelper(root.left)
        print(root.data,end=' ')
        self.__inorderHelper(root.right)

    def __delete_helper(self,root,data):
        if not root:
            return None
        if data < root.data:
            root.left = self.__delete_helper(root.left, data)
        elif data > root.data:
            root.right = self.__delete_helper(root.right, data)
        else:
            #actually delete the node

            if not root.left and not root.right:
                #no children
                root = None
                return root
            if (root.left and not root.right) or (root.right and not root.left):
                #1 child
                return root.left if root.left else root.right
            # 2 children

            succ = self.__find_succ(root,data)
            t = root.data
            root.data = succ.data
            succ.data = t
            root.right = self.__delete_helper(root.right,data)

        self.levels += 1

        return root


    def delete(self,data):
        self.levels = 0
        self.root = self.__delete_helper(self.root,data)


    def insert(self, data):
        self.levels = 0

        def insertHelper(root,data):
            if not root:
                newNode = Node.Node(data)
                root = newNode
            elif data <= root.data:
                root.left = insertHelper(root.left,data)
            else:
                root.right = insertHelper(root.right, data)
            self.levels += 1
            return root
        self.root = insertHelper(self.root,data)


    def __find_curr(self,root,data):
        if not root:
            return None
        if data == root.data:
            return root
        if data <= root.data:
            return self.__find_curr(root.left,data)
        else:
            return self.__find_curr(root.right,data)

    def __find_parent(self,root,node):
        if not root or not node:
            return None
        if root.right == node or root.left == node:
            return root
        if node.data <= root.data:
            return self.__find_parent(root.left,node)
        else:
            return self.__find_parent(root.right,node)


    def __find_min_helper(self,root):
        if not root:
            return None
        if root.left:
            return self.__find_min_helper(root.left)
        return root

    def __find_max_helper(self,root):
        if not root:
            return None
        if root.right:
            return self.__find_max_helper(root.right)
        return root


    def find_min(self):
        return self.__find_min_helper(self.root)

    def find_max(self):
        return self.__find_max_helper(self.root)

    def __is_in_subtree(self,root,node):
        if not root:
            return None
        if root == node:
            return True
        return self.__is_in_subtree(root.left,node) or self.__is_in_subtree(root.right,node)
        
    def __in_left_subtree(self,root,node):
        return self.__is_in_subtree(root.left,node)

    def __in_right_subtree(self,root,node):
        return self.__is_in_subtree(root.right,node)


    def __find_succ(self,root,data):
        #successor
        curr = self.__find_curr(root,data)
        if not curr:
            return None
        if curr.right:
            return self.__find_min_helper(curr.right)
        while True:
            parent = self.__find_parent(root,curr)
            if not parent:
                #no successor
                return None
            if self.__in_left_subtree(parent,curr):
                return parent
            else:
                curr = parent
    def find_next(self,data):
        return self.__find_succ(self.root,data)



    def find_prev(self,data):
        #predecessor
        curr = self.__find_curr(self.root,data)
        if not curr:
            return None
        if curr.left:
            return self.__find_max_helper(curr.left)

        while True:
            parent = self.__find_parent(self.root,curr)
            if not parent:
                return None
            if self.__in_right_subtree(parent,curr):
                return parent
            curr = parent


