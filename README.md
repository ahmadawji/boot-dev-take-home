# 🐍 Boot.dev Course Author Submission

Welcome to my take-home assignment submission for the **Course Author** role at [Boot.dev](https://www.boot.dev/courses/learn-python). This repository contains two sample lessons designed to fit seamlessly into the "Learn to Code in Python" curriculum.

Both lessons maintain Boot.dev's signature style: blending narrative context (Fantasy Quest), clear explanations, and hands-on coding assignments with automated test suites.

---

## 📚 Lessons Overview

### 1️⃣ Lesson 1: List Comprehensions
**Directory:** `lesson-1-list-comprehensions/`

This lesson introduces one of Python's most powerful and idiomatic features. Students learn to transition from verbose `for` loops to concise list comprehensions. 

**What's Covered:**
* Syntax and structure of a list comprehension
* Transforming existing lists into new lists
* Accessing dictionary values by key within a comprehension
* **Assignment:** Extracting item names from a list of inventory dictionaries for Fantasy Quest.

### 2️⃣ Lesson 2: Enumerate()
**Directory:** `lesson-2-enumerate/`

Building upon iteration, this lesson introduces the built-in `enumerate()` function. It teaches students the "Pythonic" way to track indices during loops, avoiding clunky C-style counter variables.

**What's Covered:**
* The pitfalls of the `range(len())` pattern
* Using `enumerate()` to unpack indices and values simultaneously
* Modifying the starting index using the `start` parameter
* **Assignment:** Formatting a list of inventory items with numbered labels (e.g., `"1. Shortsword"`) for a clean UI display.

---

## 🛠️ Repository Structure

Each lesson is self-contained in its own directory and follows a standardized 4-file structure:

- 📄 `README.md` - The lesson content, narrative, and assignment instructions (the "left side" of the screen).
- 🧑‍💻 `incomplete_main.py` - The starter code provided to the student.
- ✅ `complete_main.py` - The official solution code.
- 🧪 `test_main.py` - The automated test suite that validates the student's work.

## 🚀 Running the Tests

To test the assignments locally, navigate to either lesson directory and run the test suite:

```bash
cd lesson-1-list-comprehensions
python test_main.py
```

*Output should indicate a successful test run across all predefined test cases.*

---
*Thank you for reviewing my submission! I look forward to discussing how we can create engaging, effective lessons for future Boot.dev students.*
