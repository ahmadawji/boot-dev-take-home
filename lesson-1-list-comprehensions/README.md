# List Comprehensions

In Python, creating a new list by transforming elements of an existing list is a daily task. While you *could* use a standard `for` loop to append items one by one, Python offers a more concise, readable way to do this: **List Comprehensions**.

A list comprehension allows you to create a new list by specifying an expression and a loop in a single line.

```python
# The "Old" Way
names = ["frodo", "bilbo", "sam"]
capitalized_names = []
for name in names:
    capitalized_names.append(name.capitalize())

# The "List Comprehension" Way
capitalized_names = [name.capitalize() for name in names]
It reads almost like plain English: "Give me the capitalized version of the name, for every name in the list of names."
```

Assignment
We are building a feature for Fantasy Quest to help players manage their inventory more efficiently.

Complete the get_item_names function. It takes a list of dictionary items (where each item has a "name" key) and should return a new list containing only the strings of the item names.

Use a list comprehension to extract the "name" field from each dictionary in the items list.

Return the new list.

Tip
Don't forget that you can access dictionary values using the square bracket syntax: item["name"].