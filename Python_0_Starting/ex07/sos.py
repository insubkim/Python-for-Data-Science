import sys


NESTED_MORSE  = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.','G': '--.', 'H': '....'
                , 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.'
                , 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-'
                , 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....'
                , '6': '-....', '7': '--...', '8': '---..', '9': '----.', " ": "/ ",}

def get_morse_code(line: str) -> str:
    assert type(line) is str, 'line is not string'
    morse_code = ''
    for c in line:
        if morse_code != '':
            morse_code += ' '
        morse_code += NESTED_MORSE[c.capitalize()]
    return morse_code

print(get_morse_code(sys.argv[1]))
