from complete_main import get_item_names

def test(items, expected):
    print("---------------------------------")
    print(f"Items:\n{items}")
    print(f"Expected: {expected}")
    try:
        result = get_item_names(items)
        print(f"Actual:   {result}")
        if result == expected:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

def main():
    passed = 0
    failed = 0
    cases = [
        (
            [
                {"name": "Shortsword", "damage": 10},
                {"name": "Longbow", "damage": 15},
                {"name": "Health Potion", "healing": 25}
            ],
            ["Shortsword", "Longbow", "Health Potion"]
        ),
        (
            [
                {"name": "Leather Armor", "defense": 5},
                {"name": "Wooden Shield", "defense": 10}
            ],
            ["Leather Armor", "Wooden Shield"]
        ),
        (
            [],
            []
        ),
        (
            [
                {"name": "Magic Ring", "magic": 50, "rarity": "Legendary"}
            ],
            ["Magic Ring"]
        )
    ]

    for items, expected in cases:
        if test(items, expected):
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

if __name__ == "__main__":
    main()
