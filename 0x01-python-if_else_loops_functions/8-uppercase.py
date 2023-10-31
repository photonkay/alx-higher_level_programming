#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char
    # Print the uppercase string followed by a new line
    print(result + "\n")

# Example usage
input_string = "Hello, World!"
uppercase(input_string)
