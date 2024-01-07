import os, time, sys, math

start_time = time.time()
height = 1
ret_to_hight = 1
tree = "[SyntaxTree"
code = open("main.ehph", "r").read()
buffer = ""
reserved = {
    "print": "Function",
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
}
mode = ""
for i in range(len(code)):
    if code[i] != " ":
        buffer += code[i]
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
            name_later = tree.split("[")[::-1][0].split(" ")[0]
            tree += "["
            if name_later == "IfStatement":
                tree += "Condition"
            elif name_later == "Function":
                tree += "Arguments"
            height += 1
            ret_to_hight += 1
        if reserved[buffer] == "ArgumentCloser":
            tree += "]"
            height -= 1
            ret_to_hight -= 1
        if reserved[buffer] == "ComparisonOperator":
            tree += "[ComparisonOperator: " + buffer + "]"

        buffer = ""
    try:
        if 0 <= i < len(code):  # HOW IS THIS NOT FUCKING WORKING
            if code[i + 1] in [" ", ";", ","] or code[i + 1] in reserved:
                if buffer.startswith('"'):
                    start = i - (len(buffer) - 1)
                    print(code[start])
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


print(tree)
end_time = time.time()
run_time = int(end_time) - int(start_time)

print(
    f"""
Successfully parsed to 'FILEPLACEHOLD' in {run_time}s
"""
)
time.sleep(1)
input("Press enter to exit")
