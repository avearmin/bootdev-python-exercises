# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61362b33-a3cc-4ad7-b27c-a2dfaf6cda48/4fb8c103-5bab-4e0a-a0df-e4a024ee20b9

import random


class Stack:
    def __init__(self):
        self.arrows = []

    def push(self, arrow):
        self.arrows.append(arrow)

    def pop(self):                   # while I could have used Python's built-in method for lists 'pop()', 
        if len(self.arrows) > 0:     # I felt for purposes of the exercise it was better to write one myself
            temp = self.arrows[-1]
            del self.arrows[-1]
            return temp

    def peek(self):
        return self.arrows[-1]

    def size(self):
        return len(self.arrows)


# don't touch below this line


def main():
    stack = Stack()
    fill_stack(stack, 2)
    size_stack(stack)
    pop_stack(stack)
    pop_stack(stack)

    fill_stack(stack, 6)
    peek_stack(stack)
    peek_stack(stack)
    size_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)


def size_stack(stack):
    print("arrows size: " + str(stack.size()))
    print("=================================")
    return stack


def pop_stack(stack):
    print("popping: " + str(stack.pop()))
    print(f"arrows: {stack.arrows}")
    print("=================================")
    return stack


def peek_stack(stack):
    print("peeking: " + str(stack.peek()))
    print(f"arrows: {stack.arrows}")
    print("=================================")
    return stack


def push_stack(stack, val):
    print("pushing: " + val)
    stack.push(val)
    print(f"arrows: {stack.arrows}")
    print("=================================")
    return stack


def fill_stack(stack, num):
    random.seed(1)
    options = ["Arrow", "Fire arrow", "Ice arrow", "Oil arrow", "Lightning Arrow"]
    for i in range(num):
        optionI = random.randint(0, len(options) - 1)
        push_stack(stack, options[optionI])
    return stack


main()