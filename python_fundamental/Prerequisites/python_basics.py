import re

text = "alstha is the best in the world and his email alson@gmail.com phone is 9761856566"

# Extract email
# \b is a word boundary anchor in regex. It matches the position between a word character (like a letter, digit, or underscore) and a non-word character (like a space or punctuation), but does not consume any characters. It's useful for ensuring that, for example, a phone number is not part of a longer sequence of digits.
# {2,} is a quantifier in regex. It means "match at least 2 of the preceding element, with no upper limit." In the email regex, [a-zA-Z]{2,} matches at least 2 letters (for the domain extension, like "com", "org", etc.).

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# Extract phone number (assuming 10 digit number)
phone_pattern = r"\b\d{10}\b"
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)
