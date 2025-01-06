class Claim:
    def __init__(self, claim_id, claimant_name, claim_amount):
        self.claim_id = claim_id
        self.claimant_name = claimant_name
        self.claim_amount = claim_amount

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Claimant Name: {self.claimant_name}, Claim Amount: {self.claim_amount}"


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Claim {item.claim_id} pushed to the stack.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. No claims to process.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. No claims to show.")

    def size(self):
        return len(self.stack)


# Example usage:
stack = Stack()

# Adding some claims to the stack
stack.push(Claim(1, "John Doe", 1000.0))
stack.push(Claim(2, "Jane Smith", 1500.0))
stack.push(Claim(3, "Alice Johnson", 1200.0))

print("\nProcessing claims:")
while not stack.is_empty():
    claim = stack.pop()
    print(f"Processing {claim}")

# Checking the top claim in the stack
print("\nNext claim to be processed:")
print(stack.peek())

# Checking the size of the stack
print("\nNumber of claims remaining in the stack:")
print(stack.size())
