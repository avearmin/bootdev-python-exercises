# link to exercise: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a96ca39e-3b99-4a7a-ad9b-37c8e1a61ff6/a901fb8e-f07c-43e1-9bf4-289a5f391667

class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


def add_to_tail_test(linked_list, node):
    linked_list.add_to_tail(node)
    print(f"Adding '{node}' to tail of linked list")
    print("=================================")


def remove_from_head_test(linked_list):
    node = linked_list.remove_from_head()
    print(f"Removed '{node}' from head of linked list")
    print("=================================")
    return node


def print_linked_list(linked_list):
    print(f"Linked List:")
    print(linked_list)
    print("=================================")


def main():
    linked_list = LLQueue()
    add_to_tail_test(linked_list, Node("Sword"))
    add_to_tail_test(linked_list, Node("Bow"))
    print_linked_list(linked_list)
    add_to_tail_test(linked_list, Node("Axe"))
    add_to_tail_test(linked_list, Node("Spear"))
    print_linked_list(linked_list)
    remove_from_head_test(linked_list)
    remove_from_head_test(linked_list)
    print_linked_list(linked_list)
    remove_from_head_test(linked_list)
    remove_from_head_test(linked_list)


main()
