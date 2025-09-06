# Example 1: Custom Iterator Class
# This example demonstrates how to create a custom iterator in Python.
# An iterator is an object that implements the __iter__() and __next__() methods.

class CountDown:
    def __init__(self, start):
        # The constructor takes a starting value and initializes the current value.
        self.current = start

    def __iter__(self):
        # The __iter__ method returns the iterator object itself.
        # This is required so that the object can be used in a for loop or with the iter() function.
        return self

    def __next__(self):
        # The __next__ method returns the next value in the sequence.
        # If the countdown has reached zero or below, it raises StopIteration to signal the end.
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1  # Decrement the current value for the next iteration.
        return val

# Using the custom iterator
print("Countdown using custom iterator:")
# Here, we create a CountDown object starting from 5.
# The for loop automatically calls __iter__() and repeatedly calls __next__() until StopIteration is raised.
for num in CountDown(5):
    print(num)

# Example 2: Using iter() and next() with a built-in type

numbers = [10, 20, 30]
it = iter(numbers)
print("\nIterating using iter() and next():")
try:
    while True:
        print(next(it))
except StopIteration:
    print("Iteration finished.")

# Example 3: Iterator with __iter__ returning a separate iterator object

class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        return EvenNumbersIterator(self.max_num)

class EvenNumbersIterator:
    def __init__(self, max_num):
        self.current = 0
        self.max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.max_num:
            raise StopIteration
        return self.current

print("\nEven numbers up to 10:")
for n in EvenNumbers(10):
    print(n)


    # Example 4: Context Manager using 'with' statement
    # 
    # A context manager is a Python object that properly manages resources, such as files, by
    # automatically handling setup and cleanup actions. The most common way to use a context manager
    # is with the 'with' statement. When you enter the 'with' block, the context manager's __enter__ method is called.
    # When you exit the block (even if an exception occurs), the __exit__ method is called to clean up.
    #
    # Here, we define a custom context manager called FileOpener that opens a file and ensures it is closed properly.

    class FileOpener:
        def __init__(self, filename, mode):
            # Store the filename and mode (e.g., "r" for read, "w" for write)
            self.filename = filename
            self.mode = mode
            self.file = None  # This will hold the file object

        def __enter__(self):
            # This method is called when entering the 'with' block.
            print(f"Opening file: {self.filename}")
            self.file = open(self.filename, self.mode)  # Open the file
            return self.file  # The opened file object is returned and assigned to the variable after 'as'

        def __exit__(self, exc_type, exc_val, exc_tb):
            # This method is called when exiting the 'with' block, even if an exception occurred.
            if self.file:
                self.file.close()  # Ensure the file is closed
                print(f"Closed file: {self.filename}")
            # Returning False means exceptions (if any) are not suppressed and will propagate.
            return False

    # Usage of the context manager:
    # The following code writes to a file using our custom context manager.
    print("\nUsing custom context manager to write to a file:")
    with FileOpener("sample.txt", "w") as f:
        # Inside the 'with' block, the file is open and can be written to.
        f.write("Hello from context manager!\n")
    # After the block, the file is automatically closed.

    # Now, let's read the file using the same context manager.
    print("Reading the file using context manager:")
    with FileOpener("sample.txt", "r") as f:
        for line in f:
            # Each line is read from the file and printed (stripped of trailing newline)
            print(line.strip())
    # After this block, the file is closed again.
