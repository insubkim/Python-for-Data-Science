import sys


def get_list_len(li: list) -> int:
    assert type(li) is list, "li is not a list"
    count = 0
    for val in li:
        count += 1
    return count


def print_hex(line: str) -> None:
    assert type(line) is str, "line is not a string"
    print('[', line, ']')
    b = line.encode('ascii')
    # Convert each byte to a two-digit hex string and join them with spaces
    hex_string = ' '.join('{:02x}'.format(byte) for byte in b)
    print(hex_string)


def count_all_char(line: str) -> int:
    assert type(line) is str, "line is not a string"
    count = 0
    for c in line:
        count += 1
    return count


def count_char(line: str, array: list) -> int:
    assert type(line) is str, "line is not a string"
    assert type(array) is list, "array is not a list"
    count = 0
    for c in line:
        if c in array:
            count += 1
    return count


def line_stats(line: str):
    assert type(line) is str, 'line is not a string'
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spaces = [' ']
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                   '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\',
                   ']', '^', '_', '`', '{', '|', '}', '~']

    print('The text contains ', count_all_char(line), 'characters:')
    print(count_char(line, upper), ' upper letters')
    print(count_char(line, lower), ' lower letters')
    print(count_char(line, punctuation), ' punctuation')
    print(count_char(line, spaces), ' spaces')
    print(count_char(line, digit), ' digits')


def main():
    list_len = get_list_len(sys.argv)
    assert list_len <= 2, "more than one arg is provided to the program"
    if list_len == 1:
        print('What is the text to count?')
        line = sys.stdin.readline()
        if '\r' in line:
            line = line.replace('\r', ' ')
            print('carriage return')
    else:
        line = sys.argv[1]
    line_stats(line)


if __name__ == "__main__":
    main()
