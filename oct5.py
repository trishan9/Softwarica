# # Garbage Collection

# # Stack vs Private Heap Memory
# # Stack - Variables/Identifiers
# # Private Heap memory - Values/Objects


# # Strings, and String Manipulation
# print("Python\tWorld".expandtabs(12))
# print("Python\tWorld")
# print("Python\nWorld")
# print("Python\aWorld")  # beep code
# txt = "Hello\rWorl"  # Carriage Return
# print(txt)
# print("Hello\0World")
# print(r"Hello\tWorld")  # raw string: nullifies escape sequence characters
# print("C:\\Hello")

# a = "Hello"
# b = a.replace("H", "h")
# print(b)
# c = a.maketrans("Ho", "hO")
# print(a.translate(c))

# # Get el only from Hello using Slicing
# print(a[1::2])

# # Task
# '''
# Input: hello
# Output: wnhwnewnlwnlwno (add wn before each character)
# '''

# # First Method
# message = "hello"
# output = f"wn{message[0]}wn{message[1]}wn{message[2]}wn{message[3]}wn{message[4]}"
# print(output)

# # Another Method
# output = message.replace("h", "wnh").replace(
#     "e", "wne").replace("l", "wnl").replace("o", "wno")
# print(output)

# # Another Method
# output = message.replace("hellow", "wnhwnewnlwnlwno")
# print(output)

# # Another Method
# final = ""
# for char in message:
#     output = "wn"+char
#     final += output
# print(final)

# # Another Method
# output_list = list(map(lambda char: 'wn'+char, message))
# print("".join(output_list))

# # Another Method


# class StringManipulation:
#     '''This class contains methods for string manipulation'''  # Doc-Strings

#     def __init__(self, string):
#         self._string = string

#     def replace_string(self):
#         '''returns string by adding "wn" before each character'''
#         output_list = list(map(lambda char: 'wn'+char, self._string))
#         output = "".join(output_list)
#         return output


# print(StringManipulation.__doc__)
# new_string = StringManipulation("hello")
# print(new_string.replace_string())

# # Indentation in Python - Important


a = "123abc"

b = a.maketrans("A", "a")

print(b)
