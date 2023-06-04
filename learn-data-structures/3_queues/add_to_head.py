# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a96ca39e-3b99-4a7a-ad9b-37c8e1a61ff6/c675abc6-1091-4591-8986-43772e728447

class LinkedList:
    def add_to_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
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
        return " -> ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


def main():
    node0 = Node("Sword")
    node1 = Node("Bow")
    node2 = Node("Axe")
    node3 = Node("Spear")
    node0.set_next(node1)
    node1.set_next(node2)
    node2.set_next(node3)
    linked_list = LinkedList()
    linked_list.add_to_head(node0)
    print(linked_list)
    linked_list.add_to_head(Node("Mace"))
    print(linked_list)
    linked_list.add_to_head(Node("Dagger"))
    print(linked_list)


def set_next_test(node_lhs, node_rhs):
    node_lhs.set_next(node_rhs)
    print(f"setting '{node_rhs}' as next of '{node_lhs}'")
    print("=================================")


def add_to_tail_test(linked_list, node):
    linked_list.add_to_tail(node)
    print(f"Adding '{node}' to tail of linked list")
    print("=================================")


def add_to_head_test(linked_list, node):
    linked_list.add_to_head(node)
    print(f"Adding '{node}' to head of linked list")
    print("=================================")


def print_linked_list(linked_list):
    print(f"Linked List:")
    print(linked_list)
    print("=================================")


def main():
    linked_list = LinkedList()
    add_to_tail_test(linked_list, Node("Sword"))
    print_linked_list(linked_list)

    add_to_tail_test(linked_list, Node("Mace"))
    print_linked_list(linked_list)

    add_to_head_test(linked_list, Node("Dagger"))
    print_linked_list(linked_list)

    add_to_head_test(linked_list, Node("Bow"))
    print_linked_list(linked_list)


main()
