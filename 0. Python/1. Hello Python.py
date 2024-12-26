# Hello, Python

spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

type(spam_amount)

print(type(spam_amount))

print(type(19.95))

# True Division

print(5 / 2)
print(6 / 2)

# Floor Division
print(5 // 2)
print(6 // 2)

# Modulo
print(7 % 3)

# Exponentiation
print(2 ** 3)

# Order of operations
print(3 + 4 * 2)

# Parentheses
print((3 + 4) * 2)

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

# Min and Max
print(min(1, 2, 3))
print(max(1, 2, 3))

# Absolute Value
print(abs(32))
print(abs(-32))

# Rounding
print(round(3.14159))
print(round(3.14159, 3))

# Type Conversion
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)


