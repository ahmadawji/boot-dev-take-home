# Enumerate() in Python

When iterating over a list, you often need to keep track of the *index* (the current position) while you access the *value*. 

A common, but less "Pythonic" way to do this is using the `range(len())` pattern:

```python
# The "C-style" way
items = ["sword", "shield", "potion"]
for i in range(len(items)):
    print(f"Index {i} is {items[i]}")
This works, but it’s verbose and prone to "off-by-one" errors. In Python, we use the built-in ```enumerate()``` function to get both the index and the value simultaneously.


# The "Pythonic" way
for i, item in enumerate(items):
    print(f"Index {i} is {item}")
enumerate() returns an iterable of tuples, where each tuple contains the count (index) and the value from the original list.
```

## Assignment
In Fantasy Quest, we need to label our items in the inventory display.

Complete the label_inventory function. It takes a list of strings and should return a new list of strings where each element is formatted as: "1. ItemName", "2. ItemName", and so on.

Use ```enumerate()``` to loop through the items list.

Remember that ```enumerate()``` starts at index 0 by default. Since our display needs to start at 1, you can pass a start argument to ```enumerate()```, or simply add 1 to the index.

Return the newly formatted list of strings.