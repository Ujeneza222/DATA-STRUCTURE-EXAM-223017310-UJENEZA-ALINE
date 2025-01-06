class Claim:
    def __init__(self, claim_id, claimant_name, claim_amount, priority):
        self.claim_id = claim_id
        self.claimant_name = claimant_name
        self.claim_amount = claim_amount
        self.priority = priority

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Claimant Name: {self.claimant_name}, Claim Amount: {self.claim_amount}, Priority: {self.priority}"


def counting_sort_claims(claims):
    if not claims:
        return []

    max_priority = max(claim.priority for claim in claims)
    count = [0] * (max_priority + 1)

    for claim in claims:
        count[claim.priority] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_claims = [None] * len(claims)
    for claim in reversed(claims):
        sorted_claims[count[claim.priority] - 1] = claim
        count[claim.priority] -= 1

    return sorted_claims


# Example usage:
claims = [
    Claim(1, "John Doe", 1000.0, 2),
    Claim(2, "Jane Smith", 1500.0, 1),
    Claim(3, "Alice Johnson", 1200.0, 3),
    Claim(4, "Bob Brown", 1800.0, 2),
]

print("Claims before sorting:")
for claim in claims:
    print(claim)

sorted_claims = counting_sort_claims(claims)

print("\nClaims after sorting by priority:")
for claim in sorted_claims:
    print(claim)
