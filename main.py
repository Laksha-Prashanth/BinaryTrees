import BSTree

def main():
    print("Welcome to Binary Search Trees")
    print("1. Insert a node\n2. Delete a node\n3.Find-next\n4.Find-prev\n5.Find-min\n6.Find-max")

    tree = BSTree.Tree()
    while True:
        x = input("Waiting for input: ")
        if x == "1":
            a = input()
            tree.insert(int(a))
            
        else:
            break

        tree.printInorder()




if __name__ == "__main__":
    main()
