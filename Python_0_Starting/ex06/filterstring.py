import sys

from ft_filter import ft_filter

def f(v) -> bool:
    if v % 2:
        return False
    return True


def is_digit(c: str) ->bool:
    assert type(c) is str, '[is_digit] passed argument is not a string'

    if c == '0':
        return True

    elif c == '1':
        return True

    elif c == '2':
        return True

    elif c == '3':
        return True

    elif c == '4':
        return True

    elif c == '5':
        return True

    elif c == '6':
        return True

    elif c == '7':
        return True

    elif c == '8':
        return True

    elif c == '9':
        return True

    else:
        return False

def atoi(arg: str) -> int:
    assert type(arg) is str, '[atoi] passed argument is not a string'

    if arg[0] == '+' or arg[0] == '-':
        arg = arg[1:]

    val = 0
    for c in arg:
        if is_digit(c):
            val = val * 10 + int(c)
        else:
            assert False, '[atoi] argument is not an integer'
    return val


def get_length(line: str) -> int:
    assert type(line) is str, 'line is not a string'
    count = 0
    for c in line:
        count += 1
    return count


line = sys.argv[1]
limit = atoi(sys.argv[2])

assert type(line) is str, 'the arguments are bad'
assert type(limit) is int, 'the arguments are bad'

ft = ft_filter(lambda x: get_length(x) > limit, line.split())
print(ft)