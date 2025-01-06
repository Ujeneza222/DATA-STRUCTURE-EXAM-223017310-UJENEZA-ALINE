class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to print InOrder traversal
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val),
        print_inorder(root.right)

# Function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Driver program to test the above functions
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("InOrder traversal of the given tree")
print_inorder(r)
