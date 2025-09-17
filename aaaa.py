import re
text = "user@example.com, some.user@example.com, not_emailexample.com, exampleadress@gmail.com, email"
emails = re.findall(r"[\w.-]+@[\w-]+\.[\w-]+", text)
print(emails)