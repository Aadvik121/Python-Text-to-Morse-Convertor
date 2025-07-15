# Text to morse code dictionary for every letter, number, and a few symbols.
text_to_morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '"': '.-..-.',
    '?': '..--..',
    ';': '-.-.-',
    '-': '-...-',
    ':': '---...',
    '/': '-..-.',
    "'": '.---.',
    '(': '-.--.',
    ')': '-.--.-',
    '_': '..--.-',
    '@': '.--.-.',
    '!': '-.-.--',
    '&': '.-...',
    '=': '-...-',
    '+': '.-.-.',
    '$': '...-..-',
    'á': '.--.-',
    'ä': '.-.-',
    'é': '..-..',
    'ñ': '--.--',
    'ö': '---.',
    'ü': '..--',
    ' ': ' / '  # Word Divider
}


def convert_to_morse(text):
    full_morse = ""
    for letter in text:
        morse = text_to_morse_dict[letter.lower()]  # Convert letter to morse code

        full_morse = full_morse + ' ' + morse  # Add morse letter to full morse code

    return full_morse


input_text = input("What piece of text will you like to convert to morse?")

print(f"The morse code for this string is: {convert_to_morse(input_text)}")
