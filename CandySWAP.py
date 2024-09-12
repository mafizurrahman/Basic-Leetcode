# alice = [1, 2]
# bob  = [2,3]


class Solution:
    def fairCandySwap(self, alice, bob):
        sumalice = sum(alice)
        sumbob = sum(bob)
        diff = (sumalice - sumbob) // 2  # Calculate the difference in sums and divide by 2

        set_bob = set(bob)  # Convert bob to a set for faster lookup

        for a in alice:
            b = a - diff  # Calculate the corresponding element b
            if b in set_bob:  # Check if b exists in bob
                return [a, b]  # Return the fair swap
