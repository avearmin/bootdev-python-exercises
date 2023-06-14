# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/70432289-a136-4b2a-9d2b-962c60b95ba3

import json


class Trie:
    def words_with_prefix(self, prefix):
        # ?

    def search_level(self, cur, cur_prefix, words):
        # ?

    # don't touch below this line

    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

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


def test(words, prefix):
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print("-------------------------------------")
    words = trie.words_with_prefix(prefix)
    print(f"Words with prefix: '{prefix}':")
    for word in sorted(words):
        print(f" - {word}")
    print("=====================================")


def main():
    test(["be", "bad", "back", "bat"], "ba")
    test(["a", "to", "tea", "ted", "ten", "i", "in", "inn"], "te")


main()
