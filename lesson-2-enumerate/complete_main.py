def label_inventory(items):
    # TODO: Use enumerate() to return a new list of formatted strings
    # The format should be "1. ItemName", "2. ItemName", etc.
    # Remember you can pass a start value to enumerate(items, start=1)
    result = []
    for i, item in enumerate(items, 1):
        result.append(f"{i}. {item}")
    return result

# You can use this predefined list of items to test your function!
# Run this file directly to see the output.
if __name__ == "__main__":
    test_items = ["Shortsword", "Longbow", "Health Potion"]
    
    # Uncomment the following lines to test your code:
    print("Result:", label_inventory(test_items))
    print("Expected: ['1. Shortsword', '2. Longbow', '3. Health Potion']")
