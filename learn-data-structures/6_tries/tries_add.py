# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/820b7d02-52fd-4c94-8c62-d52242a9c438

import json


class Trie:
    def add(self, word):
        # ?

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


def test(words):
    trie = Trie()
    for word in words:
        trie.add(word)
        print(f"Adding {word}...")
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print("=====================================")


def main():
    test(["be", "bad", "back", "bat"])
    test(["a", "to", "tea", "ted", "ten", "i", "in", "inn"])


main()
