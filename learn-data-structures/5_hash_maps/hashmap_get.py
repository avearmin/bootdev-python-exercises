# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/d698f2b9-8526-4a11-9e8c-ad45890bd220/cabe4b06-1ee2-4654-9650-fb17eb0adab1

class HashMap:
    def get(self, key):
        if self.hashmap[self.key_to_index(key)] == None:
            raise Exception("sorry, key not found")
        return self.hashmap[self.key_to_index(key)][1]

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


def test(size, items, keys_to_get):
    hm = HashMap(size)
    for item in items:
        key = item[0]
        val = item[1]
        hm.insert(key, val)
    print(f"Hashmap:\n{hm}")
    print("-------------------------------------")
    for key in keys_to_get:
        try:
            val = hm.get(key)
            print(f"get({key}) -> {val}")
        except Exception as e:
            print(f"get({key}) -> {e}")
            continue
    print("=====================================")


def main():
    test(
        256,
        [
            ("apple", 1),
            ("banana", 2),
            ("cherry", 3),
            ("mango", 4),
        ],
        ["apple", "banana", "garbage"],
    )
    test(
        512,
        [
            ("golang", 1),
            ("python", 2),
            ("java", 3),
            ("javascript", 4),
            ("rust", 5),
            ("c", 6),
            ("c++", 7),
        ],
        ["golang", "python", "garbage"],
    )


main()
