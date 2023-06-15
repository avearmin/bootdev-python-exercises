# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61e9d21f-63e5-4e9f-b294-4c1972d043ab/6d67c2b9-e92a-4df2-ad2e-d0536176461e

import json


class Trie:
    def find_matches(self, document):
        matches = set() # Create a new set() to store the matches.
        for i in range(len(document)): # Loop over all the indexes of the characters in the document. Tracks the start of a substring.
            level = self.root # The current level of the trie, initalized to the root.
            for j in range(i, len(document)): # Loop over all the indexes of characters in the document, starting at the current outer index. Tracks the end of a substring.
                if document[j] not in level: # If a character is not in the level, no matches were found and we break out the inner loop.
                    break
                level = level[document[j]]
                if self.end_symbol in level: # If we find the end symbol, then we found a matching word. Add it to the set.
                    matches.add(document[i : j + 1]) # Calculate the word by slicing the document based on our outer and inner indexes.
        return matches

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
