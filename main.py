import BSTree
import AVLTree
import randomInt
import time

def main():
    inputArray = randomInt.getRandomArray()
    bstree = BSTree.Tree()
    avltree = AVLTree.AVLTree()

    bstlevels = 0

    start = time.time()
    for i in inputArray:
        bstree.insert(i)
        bstlevels += bstree.levels
    end = time.time()
    print("BSTree insertion time: ",end-start)

    avllevels = 0
    start = time.time()
    for i in inputArray:
        avltree.insert(i)
        avllevels += avltree.levels
    end = time.time()
    print("AVLTree insertion time: ",end-start)

    print("Average levels in binarysearch tree: ",bstlevels/10000)
    print("Average levels in AVL tree: ",avllevels/10000)


    bstlevels = 0
    start = time.time()
    for i in inputArray:
        bstree.delete(i)
        bstlevels += bstree.levels
    end = time.time()
    print("BSTree deletion time: ",end-start)

    avllevels = 0
    start = time.time()
    for i in inputArray:
        avltree.delete(i)
        avllevels += avltree.levels
    end = time.time()
    print("AVLTree deletion time: ",end-start)

    print("Average levels in binarysearch tree: ",bstlevels/10000)
    print("Average levels in AVL tree: ",avllevels/10000)


if __name__ == "__main__":
    main()
