class Order:
    def __init__(self, order_id, claimant_name, order_amount):
        self.order_id = order_id
        self.claimant_name = claimant_name
        self.order_amount = order_amount

    def __str__(self):
        return f"Order ID: {self.order_id}, Claimant Name: {self.claimant_name}, Order Amount: {self.order_amount}"


class TreeNode:
    def __init__(self, order):
        self.order = order
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, order):
        if self.root is None:
            self.root = TreeNode(order)
        else:
            self._insert(self.root, order)
        self.size += 1
        print(f"Order {order.order_id} inserted into the BST.")

    def _insert(self, node, order):
        if order.order_id < node.order.order_id:
            if node.left is None:
                node.left = TreeNode(order)
            else:
                self._insert(node.left, order)
        else:
            if node.right is None:
                node.right = TreeNode(order)
            else:
                self._insert(node.right, order)

    def search(self, order_id):
        return self._search(self.root, order_id)

    def _search(self, node, order_id):
        if node is None or node.order.order_id == order_id:
            return node
        elif order_id < node.order.order_id:
            return self._search(node.left, order_id)
        else:
            return self._search(node.right, order_id)

    def delete(self, order_id):
        self.root, deleted = self._delete(self.root, order_id)
        if deleted:
            self.size -= 1
            print(f"Order {order_id} deleted from the BST.")
        else:
            print(f"Order {order_id} not found in the BST.")

    def _delete(self, node, order_id):
        if node is None:
            return node, None

        if order_id < node.order.order_id:
            node.left, deleted = self._delete(node.left, order_id)
        elif order_id > node.order.order_id:
            node.right, deleted = self._delete(node.right, order_id)
        else:
            if node.left is None:
                return node.right, node
            elif node.right is None:
                return node.left, node

            temp = self._min_value_node(node.right)
            node.order = temp.order
            node.right, _ = self._delete(node.right, temp.order.order_id)

        return node, node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.order)
            self._inorder_traversal(node.right)


# Example usage:
bst = BinarySearchTree()

# Adding some orders to the BST
bst.insert(Order(1, "John Doe", 1000.0))
bst.insert(Order(2, "Jane Smith", 1500.0))
bst.insert(Order(3, "Alice Johnson", 1200.0))

# Searching for an order in the BST
order = bst.search(2)
if order:
    print(f"\nFound order: {order.order}")
else:
    print("\nOrder not found.")

# Deleting an order from the BST
bst.delete(1)

# Performing an inorder traversal of the BST
print("\nInorder traversal of the BST:")
bst.inorder_traversal()
