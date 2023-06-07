# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/36c4edda-52be-4679-a7d4-8fd81c7f7bdb/b8cf2c16-23ad-4cc0-b315-0332985f6737

import random


class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None

        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self

        if val == self.val:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            min_larger_val = self.__get_min_larger_val(val)
            self.val = min_larger_val.val
            self.right = self.right.delete(min_larger_val.val)
        
        return self
                
    def __get_min_larger_val(self, val):
        node = self.right
        while node.left:
            node = node.left
        return node

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


def test(num_characters, num_to_delete):
    characters = get_characters(num_characters)
    characters_to_delete = get_characters(num_to_delete)
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("Original Tree:")
    print(bst)
    print("-------------------------------------")
    print("Deleting characters: " + str(characters_to_delete))
    for character in characters_to_delete:
        bst = bst.delete(character)
    print("-------------------------------------")
    print("New Tree:")
    print(bst)
    print("=====================================")


def main():
    test(6, 2)
    test(12, 4)
    test(24, 6)


main()
