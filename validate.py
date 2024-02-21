special_chars = ['!', '"', '#', '$', '%', '&',
                 "'", '(', ')', '*', '+', ',', '-', '.', '/']

email = input("Enter your email address: ")
password = input("Enter your password: ")


if (not email or not password):
    print("All the fields are required!")
elif ("@" not in email or not email.endswith(".com")):
    print("Please enter a valid email address!")
elif len(password) < 8:
    print("Password must be at least 8 characters")
elif (special_chars[0] not in password) and (special_chars[1] not in password) and (special_chars[2] not in password) and (special_chars[3] not in password) and (special_chars[4] not in password) and (special_chars[5] not in password) and (special_chars[6] not in password) and (special_chars[7] not in password) and (special_chars[8] not in password) and (special_chars[9] not in password) and (special_chars[10] not in password) and (special_chars[11] not in password) and (special_chars[12] not in password) and (special_chars[13] not in password) and (special_chars[14] not in password) and (special_chars[15] not in password):
    print("Password must contain at least one special character!")
else:
    print("Validation Successful!")
