# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/61362b33-a3cc-4ad7-b27c-a2dfaf6cda48/a22849d4-4da2-497b-84c7-7d0145cbc893

def attack_action():
    call(shoot_arrow)
    call(calc_new_health)


def shoot_arrow():
    call(calc_damage)


def calc_damage():
    call(apply_damage)


# don't touch below this line


def calc_new_health():
    pass


def apply_damage():
    pass


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


stack = Stack()


def call(func):
    stack.push(func.__name__)
    print("Pushing " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")
    func()
    stack.pop()
    print("Popping " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")


call(attack_action)
