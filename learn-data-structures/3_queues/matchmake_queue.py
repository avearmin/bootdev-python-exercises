# link to exercise: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a96ca39e-3b99-4a7a-ad9b-37c8e1a61ff6/cd2268ff-f75b-4e02-ae47-148818efced1

def matchmake(queue, player):
    player_name = player[0]
    player_action = player[1]
    if player_action == 'join':
        queue.push(player_name)
    if queue.size() >= 4:
        print(f"{queue.pop()} matched {queue.pop()}!")
    if player_action == 'leave':
        queue.search_and_remove(player[0])


# don't touch below this line


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item


def test(players):
    queue = Queue()
    for player in players:
        name = player[0]
        action = player[1]
        if action == "leave":
            print(f"{name} left the queue.")
        if action == "join":
            print(f"{name} joined the queue.")
        matchmake(queue, player)
        print(f"Players in queue: {queue.items}")
        print("-------------------------------------")
    print("=====================================")


def main():
    test(
        [
            ("Alice", "join"),
            ("Bob", "join"),
            ("Charlie", "join"),
            ("David", "join"),
            ("Eve", "join"),
            ("Frank", "join"),
            ("Frank", "leave"),
            ("Grace", "join"),
        ]
    )
    test(
        [
            ("Frank", "join"),
            ("Alice", "join"),
            ("Bob", "join"),
            ("Charlie", "leave"),
            ("David", "join"),
            ("Eve", "join"),
            ("Errol", "join"),
            ("Jake", "join"),
            ("Errol", "leave"),
            ("Errol", "leave"),
            ("Grace", "join"),
        ]
    )


main()
