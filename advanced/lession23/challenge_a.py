# Extra Challenge ⭐⭐⭐

# Create:
# class PositiveNumber
#
# Implement:
# __new__(cls, value)
#
# Rules:
#
# if value < 0:
#     convert it to positive
#
# Example:
#
# number = PositiveNumber(-25)
#
# print(number)
#
# Output:
#
# 25

class PositiveNumber:
    def __new__(cls, NegativeValue):
        if NegativeValue < 0:
            NegativeValue = -NegativeValue
        instance = super().__new__(cls)
        instance.value = NegativeValue
        return instance

    def __str__(self):
        return str(self.value)
    
number = PositiveNumber(-25)
print(number)