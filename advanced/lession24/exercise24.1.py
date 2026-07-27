# Create:
# function greet()
#
# Parameter:
# name -> Optional[str]
#
# Rules:
#
# if name is None:
#     return "Hello, Guest!"
#
# otherwise:
#     return "Hello, John!"

from typing import Optional

def greet(name: Optional[str]) -> str:
    if name is None:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"

print(greet("Wellington"))  # Output: "Hello, Wellington!"
print(greet(None))  # Output: "Hello, Guest!"