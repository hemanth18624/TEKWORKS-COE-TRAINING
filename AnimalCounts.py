def accumulate_values(di, key_to_sum):
    total = 0  # Initialize the total sum

    try:
        # Iterate through each dictionary in the input tuple
        for d in di:
            # Add the value for the given key to the total, if it exists
            total += d.get(key_to_sum, 0)
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


# Sample Input
di = (
    {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
    {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
    {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
    {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67},
)

# Summing the values for 'Puppies'
key_to_sum = "Puppies"
total_puppies = accumulate_values(di, key_to_sum)

# Display the result
print(f"Total number of {key_to_sum.lower()}: {total_puppies}")
