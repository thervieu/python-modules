import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
    }

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit()
    sentence = ' '.join(sys.argv[1::])
    if all(c.isalnum() or c.isspace() for c in sentence) is False:
        print('ERROR: sentence not stricly alphanum', end='')
        sys.exit()
    sentence = ' '.join(sentence.upper().split())
    for c in sentence:
        print("{} ".format(MORSE_CODE_DICT[c]), end='')
