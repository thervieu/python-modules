import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:\n\tpython3 filterwords.py <str_to_filter> <min_length>")
    
    try:
        min_len = int(sys.argv[2])
    except:
        print("Input_error: 2nd arg must be a number")
        print("Usage:\n\tpython3 filterwords.py <str_to_filter> <min_length>")
        sys.exit()
    if min_len < 0:
        print("Input_error: 2nd arg must be positive")
        print("Usage:\n\tpython3 filterwords.py <str_to_filter> <min_length>")
        sys.exit()
        


    words = []
    word = []
    for c in sys.argv[1]:
        if c in " ,.:;[]\}\{":
            if len(word) > min_len:
                words.append(''.join(word))
            word = []
            continue
        word.append(c)
    if len(word) > min_len:
        words.append(''.join(word))
    print(words)