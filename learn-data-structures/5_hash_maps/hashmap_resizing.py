# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/d698f2b9-8526-4a11-9e8c-ad45890bd220/63a168df-81ef-4b82-804a-1e9775428081

class HashMap:
    def insert(self, key, value):
        # ?

        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        # ?

    def current_load(self):
        # ?

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


def test(items):
    hm = HashMap(0)
    for item in items:
        key = item[0]
        val = item[1]
        print(f"insert({key}, {val})")
        hm.insert(key, val)
        print(f"Load: {hm.current_load()}")
        print(f"Size: {len(hm.hashmap)}")
        print("-------------------------------------")
    print("=====================================")


def main():
    test(
        [
            ("apple", 1),
            ("banana", 2),
            ("cherry", 3),
            ("mango", 4),
            ("orange", 5),
            ("pear", 6),
            ("plum", 7),
            ("strawberry", 8),
            ("watermelon", 9),
        ]
    )


main()
