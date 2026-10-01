# original_string = "Hello World"
# new_string = original_string.replace("World", "Universe")
# print(original_string) # "Hello World"
# print(new_string) # "Hello Universe"
# original_string = new_string
# print(original_string) # "Hello Universe"


original_string = "Hello World"
new_string = original_string.upper()
print(f"After applying method:{original_string}")  # Hello World
print(f"Assign to new string:{new_string}")  # Hello Universe
original_string = new_string
print(original_string) # "Hello Universe"
