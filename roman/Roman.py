def numeral2Roman(number):
    letters = ['M', 'C', 'X', 'I']
    fives = ['', 'D', 'L', 'V']
    digits = [int(d) for d in str(number)]
    while len(digits) < 4:
        digits.insert(0, 0)

    output = ''
    for index, digit in enumerate(digits):
        if digit == 9:
            digit -= 9
            output += letters[index] + letters[index - 1]
        if digit == 4:
            digit -= 4
            output += letters[index] + fives[index]
        if digit > 4:
            digit -= 5
            output += fives[index]
        output += digit * letters[index]

    return str(output)


def roman2Numeral(roman_number):
    letters = ['M', 'C', 'X', 'I']
    fives = ['Q', 'D', 'L', 'V']

    for index, letter in enumerate(letters):
        roman_number = roman_number.replace(letter + fives[index], 4 * letter)
        roman_number = roman_number.replace(fives[index], 5 * letter)
        roman_number = roman_number.replace(letter + letters[index - 1], 9 * letter)

    output = 0
    for letter in letters:
        output *= 10
        output += roman_number.count(letter)

    return output




