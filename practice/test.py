bad_chars = [";", ":", "!", "*"]
string = "py;th*o:n!;py*t*h:o!n"
cleaned_string = ""

for char in string:
    if char in bad_chars:
        pass
    else:
        cleaned_string += char
print(cleaned_string)
