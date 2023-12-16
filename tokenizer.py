import sys

out = []

FUNC = "function"
MODE_CHANGE = "mode_change"
MATH_OP = "math_operation"
DELIMITER = "delimiter"

special = {
    ";": DELIMITER,
    "+": MATH_OP,
    "-": MATH_OP,
    "*": MATH_OP,
    "/": MATH_OP,
    "%": MATH_OP,
}
reserved_keywords = {"exit": FUNC, "print": FUNC}


def add(string):
    if string in reserved_keywords:
        out.append({"command": string, "type": reserved_keywords[string]})
    elif string in special:
        out.append({"command": string, "type": special[string]})
    else:
        out.append({"command": string, "type": "ambiguous"})


def main(file_name, do_output=False, output_dir=""):
    file = open(file_name, "r")
    content = file.read()
    file.close()

    buffer = ""
    for i in range(len(content)):
        if content[i] == " " or content[i] == "\n" or content[i] in special:
            if buffer != "":
                add(buffer)
            else:
                pass  # TODO: should there be something here?

            if content[i] in special:
                add(content[i])

            buffer = ""
        else:
            buffer += content[i]
    # TODO: add way to save "compiled" code to a file

    return out


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        main("main.ehph")
    else:
        main(argv[1])
