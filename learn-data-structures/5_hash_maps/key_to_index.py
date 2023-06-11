# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/d698f2b9-8526-4a11-9e8c-ad45890bd220/27eef24f-7b9a-41b2-81e1-d84e13eb919a

class HashMap:
    def key_to_index(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)


def test(size, keys):
    hm = HashMap(size)
    print(f"Using hashmap with size: {size}")
    for key in keys:
        index = hm.key_to_index(key)
        print(f"{key} hashes to index {index}")
    print("=====================================")


def main():
    test(4, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    test(256, ["hello", "world"])
    test(512, ["golang", "python", "java", "javascript", "rust", "c", "c++"])


main()
