# What is a type hint in Python?
#
# Type hints are a way to tell Python (and other developers, and tools like mypy) what type of value you expect for a variable, function argument, or return value.
# They do NOT change how your code runs, but they help you catch bugs, make your code easier to read, and help editors/IDEs give you better suggestions.

from typing import List, Dict, Tuple, Optional

# Example without type hints:
def add(a, b):
    """Add two values together."""
    return a + b

# You can call add(2, 3) or add("hi", "bye") and Python won't complain, but maybe you only want numbers!

# Example with type hints:
def add_numbers(a: int, b: int) -> int:
    return a + b

# Now, editors and tools can warn you if you try add_numbers("hi", "bye") because you said a and b should be int.

# More examples:

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

def total(values: List[float]) -> float:
    return sum(values)

def get_age(people: Dict[str, int], name: str) -> int:
    # people is a dictionary where keys are str and values are int
    return people.get(name, -1)

def divide(a: float, b: float) -> Tuple[float, float]:
    # Returns a tuple: (quotient, remainder)
    quotient: float = a / b
    remainder: float = a % b
    return quotient, remainder

def find_item(items: List[str], target: str) -> Optional[int]:
    # Returns the index of target in items, or None if not found
    try:
        return items.index(target)
    except ValueError:
        return None

# You can also use type hints in classes:
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age})"

# Type hints are just hints! Python will not enforce them at runtime.
# But tools like mypy can check your code for mistakes.

if __name__ == "__main__":
    print(add_numbers(3, 5))  # OK
    print(greet("Alice"))
    print(total([1.5, 2.5, 3.0]))
    people: Dict[str, int] = {"Bob": 30, "Alice": 25}
    print(get_age(people, "Alice"))
    print(divide(10, 3))
    print(find_item(["apple", "banana", "cherry"], "banana"))
    p: Person = Person("Charlie", 40)
    print(p)
    p.birthday()
    print(p)

# TL;DR: Type hints help you and your tools know what kind of data your code expects, but they don't change how Python runs your code.

