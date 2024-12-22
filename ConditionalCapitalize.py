def preLetterCase(input_string, letter):
    # Convert the string and letter to lowercase for case-insensitive comparison
    lower_string = input_string.lower()
    letter = letter.lower()

    # Find the first occurrence of the letter in the string
    index = lower_string.find(letter)

    # If the letter is not found, return the entire string in lowercase
    if index == -1:
        return input_string.lower()

    # Split the string into two parts: before and after the first occurrence of the letter
    before = input_string[:index].lower()  # Convert the part before the letter to lowercase
    after = input_string[index:].upper()  # Convert the part including and after the letter to uppercase

    # Combine and return the result
    return before + after


# Test cases
print(preLetterCase("CAtCHa", "a"))  # Output: "cATCHA"
print(preLetterCase("Preteen", "e"))  # Output: "prETEEN"
print(preLetterCase("You've got this", "m"))  # Output: "you've got this"
print(preLetterCase("Keep trying", "k"))  # Output: "KEEP TRYING"
