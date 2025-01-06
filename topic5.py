class Claim:
    def __init__(self, claim_id, claimant_name, claim_amount):
        self.claim_id = claim_id
        self.claimant_name = claimant_name
        self.claim_amount = claim_amount

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Claimant Name: {self.claimant_name}, Claim Amount: {self.claim_amount}"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_to_front(self, claim):
        new_node = Node(claim)
        new_node.next = self.head
        self.head = new_node
        print(f"Claim {claim.claim_id} added to the front of the list.")

    def add_to_end(self, claim):
        new_node = Node(claim)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Claim {claim.claim_id} added to the end of the list.")

    def remove_front(self):
        if not self.is_empty():
            removed_claim = self.head.data
            self.head = self.head.next
            print(f"Claim {removed_claim.claim_id} removed from the front of the list.")
            return removed_claim
        else:
            print("List is empty. No claims to remove.")
            return None

    def remove_end(self):
        if not self.is_empty():
            current = self.head
            if current.next is None:
                removed_claim = current.data
                self.head = None
            else:
                while current.next.next:
                    current = current.next
                removed_claim = current.next.data
                current.next = None
            print(f"Claim {removed_claim.claim_id} removed from the end of the list.")
            return removed_claim
        else:
            print("List is empty. No claims to remove.")
            return None

    def display_list(self):
        if not self.is_empty():
            current = self.head
            print("Claims in the list:")
            while current:
                print(current.data)
                current = current.next
        else:
            print("List is empty. No claims to display.")


# Example usage:
sll = SinglyLinkedList()

# Adding some claims to the list
sll.add_to_front(Claim(1, "John Doe", 1000.0))
sll.add_to_end(Claim(2, "Jane Smith", 1500.0))
sll.add_to_end(Claim(3, "Alice Johnson", 1200.0))

# Displaying the list
sll.display_list()

# Removing claims from the list
sll.remove_front()
sll.remove_end()

# Displaying the list again
sll.display_list()
