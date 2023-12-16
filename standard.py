import interpreter
import tokenizer

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
    string = get_until_eol()
    print(string)


def get_until_eol():
    to_return = []
    for i in range(len(interpreter.instructions) - interpreter.instruction_num):
        if (
            interpreter.instructions[i + interpreter.instruction_num]["type"]
            == tokenizer.DELIMITER
            and interpreter.instructions[i + interpreter.instruction_num]["command"]
            == ";"
        ):
            del to_return[0]
            return to_return
        else:
            to_return.append(interpreter.instructions[i + interpreter.instruction_num])


standard_funcs = {"print": print_func}
