from complete_main import label_inventory

def test(items, expected):
    print("---------------------------------")
    print(f"Items: {items}")
    print(f"Expected: {expected}")
    try:
        result = label_inventory(items)
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
            ["Shortsword", "Longbow", "Health Potion"],
            ["1. Shortsword", "2. Longbow", "3. Health Potion"]
        ),
        (
            ["Leather Armor", "Wooden Shield"],
            ["1. Leather Armor", "2. Wooden Shield"]
        ),
        (
            [],
            []
        ),
        (
            ["Magic Ring"],
            ["1. Magic Ring"]
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
