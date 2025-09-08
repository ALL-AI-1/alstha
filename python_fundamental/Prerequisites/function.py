# Demonstration of default arguments, keyword arguments, *args, and **kwargs

def example_func(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")

# Default arguments
example_func(1)  # a=1, b=2, c=3

# Keyword arguments
example_func(10, c=30)  # a=10, b=2, c=30

# *args and **kwargs
def demo_args_kwargs(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

demo_args_kwargs(1, 2, 3, x=100, y=200)

# Combining all together
def all_in_one(a, b=2, *args, **kwargs):
    print(f"a={a}, b={b}")
    print("Additional positional args:", args)
    if kwargs:
        key,value=next(iter(kwargs.items()))
        print("First keyword arg:", key, "=", value)
    else:
        print("No keyword arguments provided.")

all_in_one(5, 6, 7, 8, foo="bar", hello="world")

# Lambda function examples

# Simple lambda to add two numbers
add = lambda x, y: x + y
print("add(2, 3):", add(2, 3))  # Output: 5

# Lambda to square a number
square = lambda x: x ** 2
print("square(4):", square(4))  # Output: 16

# Lambda with no arguments (returns a constant)
get_hello = lambda: "Hello, Lambda!"
print("get_hello():", get_hello())  # Output: Hello, Lambda!

# Using lambda with sorted to sort by second element
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("sorted_pairs:", sorted_pairs)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# Lambda in map to double numbers
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print("doubled:", doubled)  # Output: [2, 4, 6, 8]


#recursion
# Example: Recursively sum all numbers in a nested list (arbitrary depth)
# Real-life analogy: Summing up all coins in a pile, where some coins are in boxes, and boxes may contain more boxes, etc.

def recursive_sum(items):
    total = 0
    for item in items:
        if isinstance(item, list):
            total += recursive_sum(item)  # Recursively sum nested lists
        else:
            total += item
    return total

nested_list = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
print("Sum of all numbers in nested_list:", recursive_sum(nested_list))
# Output: Sum of all numbers in nested_list: 55

# Another real-life recursion: Searching for a file in nested folders (directory tree)
def find_file(directory, target):
    """
    directory: dict, where keys are folder/file names, values are either dict (subfolder) or None (file)
    target: filename to search for
    Returns True if found, else False
    """
    for name, content in directory.items():
        if name == target and content is None:
            return True
        if isinstance(content, dict):
            if find_file(content, target):
                return True
    return False

filesystem = {
    "Documents": {
        "Resume.docx": None,
        "Projects": {
            "project1.py": None,
            "Notes.txt": None
        }
    },
    "Photos": {
        "Vacation": {
            "beach.png": None
        }
    },
    "todo.txt": None
}

print("Is 'project1.py' in filesystem?", find_file(filesystem, "project1.py"))  # True
print("Is 'missing.txt' in filesystem?", find_file(filesystem, "missing.txt"))  # False

