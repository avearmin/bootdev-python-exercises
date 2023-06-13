# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/aa5dc9d4-5286-4adf-a8c5-03e738a781a6

import json


class Trie:
    def exists(self, word):
        current = self.root
        for char in word: # Loop over each nested dictionary in the trie associated with the letters in the word.
            if char not in current:
                return False # If you get to a character that doesn't exist in the trie, return False.
            current = current[char]
        return self.end_symbol in current # Once you get to the last letter, return True 
                                          # if end_symbol is in its dictionary, and False if it isn't.
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


def test(words, words_to_check):
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print("-------------------------------------")
    for word in words_to_check:
        exists = trie.exists(word)
        print(f"'{word}' exists: {exists}")
    print("=====================================")


def main():
    test(["be", "bad", "back", "bat"], ["bad", "notfound"])
    test(["a", "to", "tea", "ted", "ten", "i", "in", "inn"], ["ted", "ten", "notfound"])


main()
