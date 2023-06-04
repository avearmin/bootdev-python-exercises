class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val


def set_next_test(node_lhs, node_rhs):
    node_lhs.set_next(node_rhs)
    print(f"setting '{node_rhs}' as next of '{node_lhs}'")
    print("=================================")


def print_linked_node(node):
    print(f" - {node}")
    if node.next:
        print_linked_node(node.next)


def print_linked_list(node):
    print(f"Linked list starting at '{node}':")
    print_linked_node(node)
    print("=================================")


def main():
    node0 = Node("Sword")
    node1 = Node("Bow")
    node2 = Node("Axe")
    node3 = Node("Spear")
    set_next_test(node0, node1)
    set_next_test(node1, node2)
    set_next_test(node2, node3)
    print_linked_list(node0)

    node4 = Node("Mace")
    set_next_test(node3, node4)
    print_linked_list(node0)

    print_linked_list(node2)


main()
