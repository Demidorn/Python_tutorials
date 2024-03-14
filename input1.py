
# Taking input from the user
name = input("Enter your name: ")
AGE = int(input("Enter your age: "))  # Convert input to integer if needed

# Using f-strings for string formatting (Python 3.6+)
print(f"Hello, {name}! You are {AGE} years old.")

# Using .format() method for string formatting
print("Hello, {}! You are {} years old.".format(name, AGE))

# Using % formatting operator
print("Hello, %s! You are %d years old." % (name, AGE))
