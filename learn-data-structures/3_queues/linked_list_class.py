class LinkedList:
    def __init__(self):
        # ?

    def __iter__(self):
        # ?

    # don't touch below this line

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        # Simple for now, will get updated
        self.head = node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


def set_next_test(node_lhs, node_rhs):
    node_lhs.set_next(node_rhs)
    print(f"setting '{node_rhs}' as next of '{node_lhs}'")
    print("=================================")


def print_linked_list(linked_list):
    print(f"Linked List:")
    print(linked_list)
    print("=================================")


def main():
    node0 = Node("Sword")
    node1 = Node("Bow")
    node2 = Node("Axe")
    node3 = Node("Spear")
    set_next_test(node0, node1)
    set_next_test(node1, node2)
    set_next_test(node2, node3)
    linked_list = LinkedList()
    linked_list.add_to_tail(node0)
    print_linked_list(linked_list)


main()

