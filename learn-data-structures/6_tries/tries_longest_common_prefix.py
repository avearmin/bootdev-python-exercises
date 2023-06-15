# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/f8a46c86-6c34-4f41-90f7-bb6f6a881b3c

import json


class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            # Iterate over the keys (children) of the current node.
            # Exclude the end symbol from consideration.
            children = []
            for key in current.keys():
                if key != self.end_symbol:
                    # Add the valid child to the children list.
                    children.append(key)
            # If the end symbol is not filtered out, it would be mistakenly considered as a valid child.
            # This would skew our results in the case of a real child and an end symbol, 
            # which should be counted as 1 but would be counted as 2.
            # Filtering out the end symbol ensures it is treated separately as a termination symbol,
            # allowing for the correct determination of the common prefix.

            # Check if there is only one valid child in the children list.
            if len(children) == 1:
                # Append the valid child to the prefix.
                prefix += children[0]
                # Update the current node to the child node.
                current = current[children[0]]
            else:
                # Exit the loop if there are more than one child, or zero valid children.
                break
        return prefix

    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    level = self.root
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


def test(words):
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print("-------------------------------------")
    lcp = trie.longest_common_prefix()
    print(f"Longest Common Prefix: {lcp}")
    print("=====================================")


def main():
    test(["bed", "ben", "be"])
    test(["grouch", "groot", "groom"])


main()
