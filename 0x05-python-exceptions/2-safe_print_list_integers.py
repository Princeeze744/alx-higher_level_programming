#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    try:
        for index in range(x):
            try:
                print("{:d}".format(my_list[index]), end="")
                print_count += 1
            except (ValueError, TypeError):
                continue
        print()
        return print_count
    except IndexError:
        raise
