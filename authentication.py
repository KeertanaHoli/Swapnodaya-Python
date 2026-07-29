users = []

def validate_password(password):

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password:

        if ch.isupper():
            has_upper = True

        elif ch.islower():
            has_lower = True

        elif ch.isdigit():
            has_digit = True

        else:
            has_symbol = True

    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        return False

    if not has_lower:
        print("Password must contain at least one lowercase letter.")
        return False

    if not has_digit:
        print("Password must contain at least one digit.")
        return False

    if not has_symbol:
        print("Password must contain at least one special symbol.")
        return False

    return True


def register():

    first_name = input("Enter First Name: ")

    if len(first_name) <= 1:
        print("First name should be more than one character.")
        return

    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")

    # Email validation
    if '@' not in email or '.' not in email:
        print("Invalid email format.")
        return

    # Warning for uppercase in email
     # Check for uppercase letters in email
    has_upper = False

    for ch in email:
        if ch.isupper():
            has_upper = True
            break

    if has_upper:
        print("Warning: Email should not contain uppercase letter.")
        return
    # Check existing user
    for user in users:
        if user["email"] == email:
            print("User already exists.")
            print("Please login.")
            return

    password = input("Enter Password: ")

    if not validate_password(password):
        return

    users.append({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    })

    print("Registration successful.")


def login():

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    for user in users:

        if user["email"] == email:

            if user["password"] == password:
                print(user["first_name"], "logged in successfully.")
            else:
                print("Either email or password doesn't match.")
                print("Please try again.")

            return

    print("User not found!")
    print("Please register.")


def forgot_password():

    email = input("Enter registered email: ")

    for user in users:

        if user["email"] == email:

            new_password = input("Enter New Password: ")

            if not validate_password(new_password):
                return

            user["password"] = new_password

            print("Your password has been updated successfully.")
            return

    print("User not found!")


while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        forgot_password()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
