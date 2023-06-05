# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a96ca39e-3b99-4a7a-ad9b-37c8e1a61ff6/795ef251-af9e-4335-a7a3-23931fd0a8ee

import random
import time


class LLQueue:
    def add_to_head(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


def benchmark(num_items):
    start = time.time()
    test(num_items)
    end = time.time()

    timeout = 1

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
    print("====================================")


def test(num_items):
    print(f"Adding {num_items} items to a linked list's head")
    linked_list = LLQueue()
    for item in get_items(num_items):
        linked_list.add_to_head(Node(item))

    print(f"Adding {num_items} items to a linked list's tail")
    linked_list2 = LLQueue()
    for item in get_items(num_items):
        linked_list2.add_to_tail(Node(item))
    print("------------------------------------")


def main():
    benchmark(10)
    benchmark(100)
    benchmark(1000)
    benchmark(10000)


def get_items(num):
    random.seed(1)
    options = ["Healing Potion", "Bandage", "Bronze Shortsword", "Bronze Gloves"]
    items = []
    for _ in range(num):
        optionI = random.randint(0, len(options) - 1)
        items.append(options[optionI])
    return items


main()
