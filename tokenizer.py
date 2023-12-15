import sys

out = []

reserved_keywords = [
    "exit"
]

def get_type():
    return "foo"


def add(string):
    if string in reserved_keywords:
        out.append({"command": string, "type": get_type(string)})


def main(file_name, do_output=False, output_dir=""):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    
    buffer = ""
    for i in range(len(content)):
        if content[i] == " ":
            add(buffer)
            buffer = ""
        else:
            buffer += content[i]
    
    return out
    

        

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        main('main.ehph')
    else:
        main(argv[1])
