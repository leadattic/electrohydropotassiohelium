"""
All functions included in the base version of ElHyPoHe are defined here
"""


def throw(str):  # This function is also called when the interpreter encounters an error
    print("\033[91mERROR: " + str)
    exit(1)


def warn(str):
    print("\033[93mWARN: " + str)


def exit_func(code):
    exit(code)


def print_func():
    str = "test"
    print(str)


standard_funcs = {"print": print_func}
