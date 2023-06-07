# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/36c4edda-52be-4679-a7d4-8fd81c7f7bdb/dc322f0d-3821-44a9-a628-d7e5207ca839

import random


class BSTNode:
    def get_min(self):
        # ?

    def get_max(self):
        # ?

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
    random.seed(1)
    characters = []
    for _ in range(num):
        character = Character(random.randint(0, num - 1))
        characters.append(character)
    return characters


def test(num_characters):
    characters = get_characters(num_characters)
    bst = BSTNode()
    for character in characters:
        print(f"Inserting {character} into tree...")
        bst.insert(character)
    print("Tree:")
    print("-------------------------------------")
    print(bst)
    print("-------------------------------------")
    print(f"Character with smallest gamertag: {bst.get_min()}")
    print(f"Character with largest gamertag: {bst.get_max()}")
    print("=====================================")


def main():
    test(5)
    test(10)
    test(20)


main()
