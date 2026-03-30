def check(username, password):
    if not username or not password:
        return False
    if len(password) < 8:
        return False
    return True

user2 = input("Enter your username:  ")
password2 = input("Enter your password: ")

if check(user2, password2):
    print("Credentials are valid")
else:
    print("Invalid username or password")