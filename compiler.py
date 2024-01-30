import os, tokenizer, sys


def main():
    c_code = ("""
#include <stdio.h>
#include <stdint.h>

#FUNCTION_SPACE


int main(void){
    #CODE_SPACE
}
""")
    c_functions = ""

    standard_file = open("std/standard.h", "r")
    c_functions += standard_file.read()
    standard_file.close()

    code = tokenizer.get_tree()
    print(code)

    c_code = c_code.replace("#FUNCTION_SPACE", c_functions)
    for i in range(len(code)):
        pass

    print(c_code)


def string_to_array(str):  # Turns a string into a string of all the chars in the string
    output = "["
    for i in range(len(str)):
        output += "'" + str[i] + "',"
    output = output[:-1] + "]"
    return output


if __name__ == "__main__":
    main()
