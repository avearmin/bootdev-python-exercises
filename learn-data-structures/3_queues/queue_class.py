import random


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        # ?

    def pop(self):
        # ?

    def peek(self):
        # ?

    def size(self):
        # ?


# don't touch below this line


def main():
    queue = Queue()
    fill_queue(queue, 2)
    size_queue(queue)
    peek_queue(queue)
    pop_queue(queue)
    pop_queue(queue)

    fill_queue(queue, 6)
    size_queue(queue)
    peek_queue(queue)
    peek_queue(queue)
    pop_queue(queue)
    pop_queue(queue)
    pop_queue(queue)
    pop_queue(queue)
    pop_queue(queue)
    pop_queue(queue)


def size_queue(queue):
    print("items size: " + str(queue.size()))
    print("=================================")
    return queue


def pop_queue(queue):
    print("popping: " + str(queue.pop()))
    print(f"items: {queue.items}")
    print("=================================")
    return queue


def peek_queue(queue):
    print("peeking: " + str(queue.peek()))
    print(f"items: {queue.items}")
    print("=================================")
    return queue


def push_queue(queue, item):
    queue.push(item)
    print("pushing: " + item)
    print(f"items: {queue.items}")
    print("=================================")
    return queue


def fill_queue(queue, num):
    random.seed(1)
    options = ["Spear", "Bow", "Mace", "Axe", "Sword"]
    for i in range(num):
        optionI = random.randint(0, len(options) - 1)
        push_queue(queue, options[optionI])
    return queue


main()
