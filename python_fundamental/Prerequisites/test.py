# # # "isinstance" is a built-in Python function used to check if an object is an instance of a particular class or a tuple of classes.
# # # Syntax: isinstance(object, classinfo)
# # # Returns True if the object is an instance of the classinfo, otherwise False.

# # # Example:
# # x = 5
# # print(isinstance(x, int))  # True, because x is an integer

# # y = [1, 2, 3]
# # print(isinstance(y, list))  # True, because y is a list

# # # You can also check against a tuple of types:
# # print(isinstance(x, (float, int, str)))  # True, because x is an int (one of the types in the tuple)

# # # In the server.py file, you can see the use of isinstance to check if the payload is a dict:
# # # if isinstance(payload, dict):
# # #     data_store.update(payload)
# # # else:
# # #     data_store["value"] = payload

# # # Let's demonstrate a similar pattern here:

# # payload = {"name": "Alice", "age": 30}
# # if isinstance(payload, dict):
# #     print("Payload is a dictionary. Keys:", list(payload.keys()))
# # else:
# #     print("Payload is not a dictionary. Value:", payload)

# # payload2 = [1, 2, 3]
# # if isinstance(payload2, dict):
# #     print("Payload2 is a dictionary.")
# # else:
# #     print("Payload2 is not a dictionary. Value:", payload2)

# #     # payload = request.get_json() or {} means:
# #     # Try to get the JSON data from the request body.
# #     # If the request does not contain valid JSON (i.e., get_json() returns None),
# #     # then use an empty dictionary {} as a fallback.
# #     # This ensures that 'payload' is always a dictionary (or at least not None),
# #     # which helps prevent errors when accessing or updating it later in the code.
# #     #
# #     # Example:
# #     # If the request body is '{"foo": "bar"}', then payload will be {'foo': 'bar'}.
# #     # If the request body is empty or not valid JSON, then payload will be {}.

# #     # In Flask, `jsonify` is a helper function that creates a Response object with the JSON representation of the data you pass to it.
# #     # It also sets the correct Content-Type header to "application/json".
# #     # Example:
# #     # from flask import jsonify
# #     # return jsonify({"message": "Hello, world!"})
# #     # This will return a JSON response: {"message": "Hello, world!"}


# # a={"foo": "bar","hello": "world","aa":1}

# # aa=iter(a.items())
# # print(next(aa))
# # print(next(aa))

# # def demo_args_kwargs(v,*args, **kwargs):
# #     print("Positional arguments (args):", args)
# #     print("Keyword arguments (kwargs):", kwargs)
# #     kwargs_list=list(kwargs.items())
# #     print(kwargs_list)
# #     # The original code tries to access kwargs_list["y"], but kwargs_list is a list of tuples, not a dict.
# #     # To get the value for key "y", you can use kwargs["y"] or search the list.
# #     print(kwargs["y"])
# # a=4
# # demo_args_kwargs(a, 2, 3, x=100, y=200)

# a = [1, 2, 3, 4]
# b = ["LA", "SDK"]
# C = list(zip(a, b))
# print(C)

# a=[(1,5),(2,3),(3,4),(4,2)]
# # The 'key' argument in sorted() specifies a function that determines how the elements are compared for sorting.
# # Here, key=lambda x: x[1] means sorting the list of tuples by the second element of each tuple.
# print(sorted(a, key=lambda x: x[1]))

# # .map() is a built-in Python function that applies a given function to each item in an iterable (like a list) and returns a map object (which can be converted to a list).
# # Example: Double each number in a list
# nums = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, nums))
# print("Doubled numbers using map():", doubled)  # Output: [2, 4, 6, 8]
# # Simple example of map: square each number in a list (no lambda)
# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(square, numbers))
# print("Squared numbers using map():", squared)  # Output: [1, 4, 9, 16, 25]

# from pathlib import Path
# try:
#     p = Path(r"F:/REAL_PROJECTS/All_AI/text.txt")
#     if p.exists():
#         print("File content using pathlib:", p.read_text())
#     else:
#         print("File does not exist for pathlib demo.")
# except Exception as e:
#     print("Error in pathlib file handling:", e)

# Find a duplicate in the list and print all indices of that duplicate
# numbers = [3, 6, 2, 4, 3, 6, 8, 9]
# duplicate = None

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             duplicate = numbers[i]
#             break
#     if duplicate is not None:
#         break

# for i in range(len(numbers)):
#     if numbers[i] == duplicate:
#         print(i)

for i in 6:
    print(ord(i))
