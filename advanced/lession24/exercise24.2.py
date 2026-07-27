# Create:
# function calculate_square()
#
# Parameter:
# value -> int | float
#
# Return:
# value²

def calculate_square(value: int | float) -> float:
    return value * value

print(f"{calculate_square(256.72)}")