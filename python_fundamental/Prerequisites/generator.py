# import sys

# # Regular function with return
# def get_squares_return(n):
#     squares = []
#     for i in range(n):
#         squares.append(i * i)
#     return squares

# # Generator function with yield
# def get_squares_yield(n):
#     for i in range(n):
#         yield i * i

# # Test with 1000 numbers
# n = 1000

# # Using return
# squares_list = get_squares_return(n)
# print(f"List memory usage: {sys.getsizeof(squares_list)} bytes")

# # Using yield
# squares_gen = get_squares_yield(n)
# print(f"Generator memory usage: {sys.getsizeof(squares_gen)} bytes")

# def create_generator(n):
#     for i in range(n):
#         yield i * 2  # Pauses here and returns value

# # Create generator object
# numbers = create_generator(5)  # n = 5
# for i in numbers:
#     print (i)
# print("done")
# print("start")
# for i in numbers:
#     print (i)

# import sys

# # Generator approach
# def create_generator(n):
#     for i in range(n):
#         yield i * 2

# # List comprehension approach
# def create_list(n):
#     return [i * 2 for i in range(n)]

# n = 1000000

# # Generator + list conversion
# gen = create_generator(n)
# gen_list = list(gen)
# print(f"Generator approach: {sys.getsizeof(gen_list)} bytes")

# # Direct list creation
# direct_list = create_list(n)
# print(f"Direct list: {sys.getsizeof(direct_list)} bytes")