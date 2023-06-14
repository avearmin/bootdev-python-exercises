# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/6d67c2b9-e92a-4df2-ad2e-d0536176461e

import json


class Trie:
    def find_matches(self, document):
        # ?

    # don't touch below this line

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


def test(words, document):
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print("-------------------------------------")
    matches = trie.find_matches(document)
    print(f"Document: '{document}'")
    print("Matches:")
    for match in sorted(matches):
        print(f" - {match}")
    print("=====================================")


def main():
    test(["bad", "baddie", "badguy", "suck"], "the badguy really sucks")
    test(["be", "bad", "back", "bat"], "he is back at bat")


main()
