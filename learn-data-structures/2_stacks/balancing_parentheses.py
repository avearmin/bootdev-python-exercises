def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == ')' and stack.peek() is None:
            return False
        elif char == '(':
            stack.push(char)
        elif char == ')':
            stack.pop()
    return stack.peek() is None


# don't modify below this line


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


def test(input_str):
    print(f"Input: {input_str}")
    print(f"Output: {is_balanced(input_str)}")
    print("=================================")


def main():
    test("(")
    test("()")
    test("(())")
    test("()()")
    test("(()))")
    test("((())())")


main()