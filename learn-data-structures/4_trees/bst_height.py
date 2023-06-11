# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/36c4edda-52be-4679-a7d4-8fd81c7f7bdb/59717501-d833-4c2c-a0e1-1938eaf97326

import random


class BSTNode:
    def height(self):
        if self == None: # If the current node is None, it represents an empty tree, 
            return 0     # so its height is 0.
        
        left_count = 0 # Initalize our left count at 0.
        if self.left:
            left_count = self.left.height() # Recursively calculates the left subtree.
        
        right_count = 0 # Initalize our right count at 0.
        if self.right:
            right_count = self.right.height() # Recursively calculates the right subtree.

        return max(left_count, right_count) + 1 # Our method resloves after each branch
                                                # has been fully explored. We return the larger
                                                # value + 1 to account for the longest branch +
                                                # its root node. It should be noted that when a 
                                                # node has no branches of its own, it is the end 
                                                # of its parent branch and simply returns as 1 
                                                # max(0, 0) + 1.

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def __repr__(self):
        lines = []
        print_tree(self, lines)
        return "\n".join(lines)


class Character:
    def __init__(self, gamertag):
        self.gamertag = gamertag
        character_names = [
            "Ebork",
            "Astram",
            "Elian",
            "Tarlock",
            "Grog",
            "Myra",
            "Sullivan",
            "Marlo",
            "Jax",
            "Anthony",
            "Bhurdan",
            "Thoreuth",
            "Bob",
            "Varis",
            "Nyx",
            "Luna",
            "Ash",
            "Rhogar",
            "Ember",
            "Mikel",
            "Yamil",
            "Velithria",
        ]
        self.character_name = (
            f"{character_names[gamertag%len(character_names)]}#{gamertag}"
        )

    def __eq__(self, other):
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(bst_node, lines, level=0):
    if bst_node != None:
        print_tree(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        print_tree(bst_node.left, lines, level + 1)


def get_characters(num):
    characters = []
    for _ in range(num):
        character = Character(random.randint(0, num - 1))
        characters.append(character)
    return characters


def test(num_characters):
    characters = get_characters(num_characters)
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("Tree:")
    print(bst)
    print("-------------------------------------")
    print(f"Height: {bst.height()}")
    print("=====================================")


def main():
    random.seed(1)
    test(1)
    test(3)
    test(10)
    test(20)


main()
