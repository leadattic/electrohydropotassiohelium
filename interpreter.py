import os
import sys
import math
import tokenizer
import standard as std

mode = 0

functions = {}


def main():
    instructions = tokenizer.main("main.ehph")  # TODO: should take argv

    for i in range(len(instructions)):
        instruction = instructions[i]
        handle(instruction["command"], instruction["type"])


def handle(command, type):  # This should work like in C
    if type == tokenizer.MODE_CHANGE:
        mode_change_handler(command)
    elif type == tokenizer.FUNC:
        run_function(command)  # TODO: How to handle args? :(
    elif type == tokenizer.DELIMITER:
        pass
    else:
        std.throw("'" + command + "' is not recognized as a command of any type")


def mode_change_handler(command):
    pass  # TODO: consider if type should exist


def run_function(command):
    if command.lower() in std.standard_funcs:
        std.standard_funcs[command.lower()]()
    elif command.lower() in functions:
        for i in range(len(functions[command.lower()])):
            instruction = functions[command.lower()][i]
            handle(instruction["command"], instruction["type"])
    else:
        std.throw("'" + command + "' is not recognized as a command of any type")


if __name__ == "__main__":
    main()
