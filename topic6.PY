class Claim:
    def __init__(self, claim_id, claimant_name, claim_amount):
        self.claim_id = claim_id
        self.claimant_name = claimant_name
        self.claim_amount = claim_amount

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Claimant Name: {self.claimant_name}, Claim Amount: {self.claim_amount}"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def display_tree(self, level=0):
        print(' ' * level * 4 + str(self.data))
        for child in self.children:
            child.display_tree(level + 1)


# Example usage:
root_claim = Claim(0, "Root", 0.0)
root = TreeNode(root_claim)

# Adding some claims to the tree
claim1 = TreeNode(Claim(1, "John Doe", 1000.0))
claim2 = TreeNode(Claim(2, "Jane Smith", 1500.0))
claim3 = TreeNode(Claim(3, "Alice Johnson", 1200.0))

root.add_child(claim1)
root.add_child(claim2)
claim1.add_child(claim3)

# Displaying the tree
print("Claims Hierarchical Tree:")
root.display_tree()
