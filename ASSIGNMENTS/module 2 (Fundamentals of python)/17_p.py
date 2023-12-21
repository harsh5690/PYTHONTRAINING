#Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.
def swap_strings(str1, str2):
    # Check if the input strings have at least 2 characters
    if len(str1) < 2 or len(str2) < 2:
        return "Strings should have at least 2 characters."
    
    # Swap the first two characters of each string
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    
    # Concatenate the modified strings with a space in between
    result = new_str1 + " " + new_str2
    return result

# Test the function
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = swap_strings(string1, string2)
print("Result:", result)
