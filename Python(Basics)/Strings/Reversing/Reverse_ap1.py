def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

string =input()
reversed_string = reverse_string(string)
print(reversed_string)