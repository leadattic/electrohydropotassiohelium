import os, time, sys, math

DEBUG = False
start_time = time.time()
height = 1
ret_to_hight = 1
tree = "[SyntaxTree"
code = open("main.ehph", "r").read()
buffer = ""
reserved = {  # ALL LIBRARIES should be added to this, but with their
    "print": "Function",
    "exit": "Function",
    ";": "eol",
    "if": "IfStatement",
    "+": "ArithmaticOperator",
    "-": "ArithmaticOperator",
    "*": "ArithmaticOperator",
    "/": "ArithmaticOperator",
    ",": "ArgumentSeparator",
    "(": "ArgumentOpener",
    ")": "ArgumentCloser",
    "==": "ComparisonOperator",
    "=!": "ComparisonOperator",
    "{": "CodeSectionStart",
    "}": "CodeSectionEnd",
}

for i in range(len(code)):
    if code[i] not in ["\n", " "]:  # TODO:  Consider
        buffer += code[i]
    if DEBUG:
        print(buffer)
    if buffer in reserved:
        if reserved[buffer] == "IfStatement":
            tree += "[IfStatement"
            height += 1
            ret_to_hight += 1
        if reserved[buffer] == "Function":
            height += 1
            tree += "[Function " + buffer
        if reserved[buffer] == "eol":
            for j in range(height - ret_to_hight):
                tree += "]"
            height = ret_to_hight
        if reserved[buffer] == "ArithmaticOperator":
            tree += "[ArithmaticOperator: " + buffer + "]"
        if reserved[buffer] == "ArgumentSeparator":
            if code[::-1][0] == "]":
                for j in range(height - ret_to_hight):
                    tree += "]"
                    height = ret_to_hight
        if reserved[buffer] == "ArgumentOpener":
            parent_type = tree.split("[")[::-1][0].split(" ")[
                0
            ]  # Consider renaming parent_type
            tree += "["
            if parent_type == "IfStatement":
                tree += "Condition"
            elif parent_type == "Function":
                tree += "Arguments"
            height += 1
            ret_to_hight += 1
        if reserved[buffer] == "ArgumentCloser":
            tree += "]"
            height -= 1
            ret_to_hight -= 1
        if reserved[buffer] == "ComparisonOperator":
            tree += "[ComparisonOperator: " + buffer + "]"
        if reserved[buffer] == "CodeSectionStart":
            tree += "[Code "
            height += 1
            ret_to_hight += 1
        if reserved[buffer] == "CodeSectionEnd":
            tree += "]]"
            height -= (
                2  # Having these values be 2 might cause bugs in the future, beware
            )
            ret_to_hight -= 2

        buffer = ""
    try:
        if 0 <= i < len(code):  # HOW IS THIS NOT FUCKING WORKING
            if code[i + 1] in [" ", ";", ","] or code[i + 1] in reserved:
                if buffer.startswith('"'):
                    start = i - (len(buffer) - 1)

                    quotation_count = 0
                    j = 0
                    string_buffer = ""
                    while quotation_count != 2:
                        if code[start + j] != '"':
                            string_buffer += code[start + j]
                        else:
                            quotation_count += 1
                        j += 1
                    tree += "[StringLiteral: " + string_buffer + "]"
                elif buffer.isdigit():
                    tree += "[IntegerLiteral: " + buffer + "]"
                buffer = ""
    except IndexError as e:
        print("Out of index, handled")

    if len(code) == i:
        for j in range(ret_to_hight - 1):
            tree += "]"


def get_tree():
    return tree


end_time = time.time()
run_time = int(end_time) - int(start_time)


if __name__ == "__main__":
    print(tree)
    time.sleep(1)
    input("Press enter to exit")
    print(f"Successfully parsed in {run_time}s")
