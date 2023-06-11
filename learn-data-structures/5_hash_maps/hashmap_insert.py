# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/d698f2b9-8526-4a11-9e8c-ad45890bd220/fe0bc417-69dc-435e-95c8-79cd8dde04a0

class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = (key, value)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)


def test(size, items):
    hm = HashMap(size)
    print(f"Using hashmap with size: {size}")
    for item in items:
        key = item[0]
        val = item[1]
        hm.insert(key, val)
        print(f"Inserted ({key}, {val})")
    print(f"Final hashmap:\n{hm}")
    print("=====================================")


def main():
    test(1, [("apple", 1), ("banana", 2)])
    test(4, [("apple", 1), ("banana", 2)])
    test(8, [("apple", 1), ("banana", 2), ("apple", 592), ("banana", 54)])


main()
