def align_right(a_string, string_length):
    spaces = string_length - len(a_string)
    return " " * 4 + a_string

print(align_right("CS1301", 10))