# Author: Gleb Ignatski
import sys

error = "Sorry, but the range is between 1 and the number of lines in the code which is"

def overwriteFile(file_name, new_code):
    with open(file_name, 'w') as f:
        f.write("")
    with open(file_name, 'w') as f:
        f.write(new_code)

def getFileLines(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
    return lines

def indent(lines, start, finish):
    new_code = ""
    tab = "    "
    if start >= 0 and finish <= len(lines):
        for i in range(len(lines)):
            if (i >= (start-1) and i < finish):
                new_code = new_code + tab + lines[i]
            else:
                new_code = new_code + lines[i]
        return new_code
    else:
        print("{} {}.".format(error, len(lines)))
        return "error"

def unindent(lines, start, finish):
    new_code = ""
    if start >= 0 and finish <= len(lines):
        for i in range(len(lines)):
            if (i >= (start-1) and i < finish):
                if (len(lines[i]) > 3 and lines[i][0:4] == "    "):
                    new_code = new_code + lines[i][4:]
                else:
                    new_code = new_code + lines[i]
            else:
                new_code = new_code + lines[i]
        return new_code
    else:
        print("{} {}.".format(error, len(lines)))
        return "error"

if __name__ == "__main__":
    file_name = sys.argv[1]
    try:
        arg = sys.argv[5] # implies user wants to edit their file in safe mode
    except:
        arg = ""

    if sys.argv[2] == "i":
        lines = getFileLines(file_name)
        new_code = indent(lines, int(sys.argv[3]), int(sys.argv[4]))
        if new_code != "error":
            if arg == "":
                overwriteFile(file_name, new_code)
            else:
                # creates a file with the overwritten code that you can paste into your target file
                with open("indented_code.txt", 'w+') as f:
                    f.write(new_code)

    if sys.argv[2] == "u":
        lines = getFileLines(file_name)
        new_code = unindent(lines, int(sys.argv[3]), int(sys.argv[4]))
        if new_code != "error":
            if arg == "":
                overwriteFile(file_name, new_code)
            else:
                # creates a file with the overwritten code that you can paste into your target file
                with open("unindented_code.txt", 'w+') as f:
                    f.write(new_code)
