# program for string to double conversion
string_input = input("Enter a string representation of a number: ")

try:
    double_output = float(string_input)
    print("The string input converted to double is:", double_output)
except ValueError:
    print("Error: The input is not a valid number.")
