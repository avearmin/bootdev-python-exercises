# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/dd146e90-6275-448a-89c4-d148e52ab022

import json


class Trie:
    def advanced_find_matches(self, document, variations):
        # ?

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


def test(words, document, variations):
    trie = Trie()
    for word in words:
        print(f" - Adding '{word}' to trie")
        trie.add(word)
    matches = trie.advanced_find_matches(document, variations)
    print(f"Document: '{document}'")
    print("Variations:")
    for key in sorted(variations):
        print(f" - {key} -> {variations[key]}")
    print("Matches:")
    for match in sorted(matches):
        print(f" - {match}")
    print("=====================================")


def main():
    test(
        [
            "darn",
            "nope",
            "bad",
        ],
        "This is a d@rn1t test with b@d words!",
        {
            "@": "a",
            "1": "i",
            "4": "a",
            "!": "i",
        },
    )
    test(
        [
            "dang",
            "darn",
            "heck",
            "gosh",
        ],
        "d@ng it to h3ck",
        {
            "@": "a",
            "3": "e",
        },
    )


main()
