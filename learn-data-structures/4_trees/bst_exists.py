# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/36c4edda-52be-4679-a7d4-8fd81c7f7bdb/f4ec8c86-2c5f-455e-9f3b-64354085d328

import random


class BSTNode:
    def exists(self, val):
        if self.val == val:
            return True

        if val < self.val and self.left is not None:
            return self.left.exists(val)

        if val > self.val and self.right is not None:
            return self.right.exists(val)

        return False

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
    character = get_characters(num_characters)[0]
    print(f"{character} exists: { bst.exists(character) }")
    print("=====================================")


def main():
    random.seed(1)
    test(3)
    test(4)
    test(5)
    test(6)


main()
