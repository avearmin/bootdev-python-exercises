# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/36c4edda-52be-4679-a7d4-8fd81c7f7bdb/e044c349-8b8f-4289-b1a6-a38963532adf

import random


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # ?

    # don't touch below this line

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
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
        if not isinstance(other, Character):
            return False
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        if not isinstance(other, Character):
            return False
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        if not isinstance(other, Character):
            return False
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(node, lines, level=0):
    if node.val is not None:
        print_tree(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        print_tree(node.left, lines, level + 1)


def get_characters(num):
    characters = []
    for _ in range(num):
        character = Character(random.randint(1, num - 1))
        characters.append(character)
    return characters


def test(num_characters):
    characters = get_characters(num_characters)
    tree = RBTree()
    for character in characters:
        print(f"Inserting {character} into tree...")
        tree.insert(character)
    print("Tree:")
    print("-------------------------------------")
    print(tree)
    print("=====================================")


def main():
    random.seed(1)
    test(4)
    test(8)
    test(16)


main()
