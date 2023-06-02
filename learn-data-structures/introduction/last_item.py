# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a9d59658-4e3c-441e-973b-147cc3c7e9de/21630e80-ca7b-40d1-b552-926d84bd783b

import random


def last_item(inventory):
    # ?


# don't touch below this line


def get_inventory(num):
    random.seed(1)
    options = [
        "Short sword",
        "Bread",
        "Healing potion",
        "Leather scraps",
        "Chainmail Armor",
    ]
    inventory = []
    for i in range(num):
        optionI = random.randint(0, len(options) - 1)
        inventory.append(options[optionI])
    return inventory


def test(num):
    inventory = get_inventory(num)
    print(f"Total items in Inventory: {num}")
    print(f"Last item in Inventory: {last_item(inventory)}")
    print("=================================")


def main():
    test(10)
    test(100)
    test(1000)
    test(10000)
    test(100000)


main()
