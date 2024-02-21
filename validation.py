from string import punctuation

database = {
    "mailtotrishan@gmail.com": "trishan1122@",
    "example@gmail.com": "password@"
}

attempts_left = 3
special_chars = list(punctuation)
is_password_valid = False

while attempts_left != 0:
    print(
        f"\nPlease login using your email address and password: Attempts Left: {attempts_left}")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    for char in password:
        if (char in special_chars):
            is_password_valid = True
            break

    try:
        user = database[email]
        if user:
            user_exists = True
    except KeyError:
        user_exists = False

    if not email or not password:
        print("All fields are required")
        attempts_left -= 1
    elif not email.endswith("@gmail.com"):
        print("Please enter valid email address")
        attempts_left -= 1
    elif not user_exists:
        print("User with this email address doesn't exists!")
        attempts_left -= 1
    elif len(password) < 8 or not (is_password_valid):
        print("Password must be valid")
        attempts_left -= 1
    elif password != database[email]:
        print("Password is incorrect!")
        attempts_left -= 1
    else:
        break
else:
    print("You are blocked because your all all attempts are failed!")

if attempts_left != 0:
    print('Logged in Succesfully!')
