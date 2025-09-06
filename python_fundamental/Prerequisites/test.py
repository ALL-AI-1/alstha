# "isinstance" is a built-in Python function used to check if an object is an instance of a particular class or a tuple of classes.
# Syntax: isinstance(object, classinfo)
# Returns True if the object is an instance of the classinfo, otherwise False.

# Example:
x = 5
print(isinstance(x, int))  # True, because x is an integer

y = [1, 2, 3]
print(isinstance(y, list))  # True, because y is a list

# You can also check against a tuple of types:
print(isinstance(x, (float, int, str)))  # True, because x is an int (one of the types in the tuple)

# In the server.py file, you can see the use of isinstance to check if the payload is a dict:
# if isinstance(payload, dict):
#     data_store.update(payload)
# else:
#     data_store["value"] = payload

# Let's demonstrate a similar pattern here:

payload = {"name": "Alice", "age": 30}
if isinstance(payload, dict):
    print("Payload is a dictionary. Keys:", list(payload.keys()))
else:
    print("Payload is not a dictionary. Value:", payload)

payload2 = [1, 2, 3]
if isinstance(payload2, dict):
    print("Payload2 is a dictionary.")
else:
    print("Payload2 is not a dictionary. Value:", payload2)

    # payload = request.get_json() or {} means:
    # Try to get the JSON data from the request body.
    # If the request does not contain valid JSON (i.e., get_json() returns None),
    # then use an empty dictionary {} as a fallback.
    # This ensures that 'payload' is always a dictionary (or at least not None),
    # which helps prevent errors when accessing or updating it later in the code.
    #
    # Example:
    # If the request body is '{"foo": "bar"}', then payload will be {'foo': 'bar'}.
    # If the request body is empty or not valid JSON, then payload will be {}.

    # In Flask, `jsonify` is a helper function that creates a Response object with the JSON representation of the data you pass to it.
    # It also sets the correct Content-Type header to "application/json".
    # Example:
    # from flask import jsonify
    # return jsonify({"message": "Hello, world!"})
    # This will return a JSON response: {"message": "Hello, world!"}
