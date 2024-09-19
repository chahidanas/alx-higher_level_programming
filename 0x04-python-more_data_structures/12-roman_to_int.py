#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    
    # Roman numerals map
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Invalid cases: empty string or invalid characters
    if not roman_string:
        return 0
    
    numbers = [data.get(char, 0) for char in roman_string]
    
    # Return 0 if any invalid Roman numeral character is found
    if 0 in numbers:
        return 0
    
    # Conversion logic
    rep = 0
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            rep += numbers[i]
        else:
            rep -= numbers[i]
    rep += numbers[-1]
    
    return rep

