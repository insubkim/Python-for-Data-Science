import sys


def get_list_len(li: list) -> int:
    assert type(li) is list, "[get_list_len] is not a list"
    count = 0
    for val in li:
        count += 1
    return count


def main():
    assert len(sys.argv) == 2, "more than one arg is provided to the program"


if __name__ == "__main__":
    main()
