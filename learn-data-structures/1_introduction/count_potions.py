# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a9d59658-4e3c-441e-973b-147cc3c7e9de/d2176e10-f96b-4f57-af5c-e03e5c46fc88

import random


def count_potions(inventory):
    count = 0
    for item in inventory:
        if item == "Healing potion":
            count += 1
    return count


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
    print(f"Number of potions: {count_potions(inventory)}")
    print("=================================")


def main():
    test(10)
    test(100)
    test(1000)
    test(10000)


main()