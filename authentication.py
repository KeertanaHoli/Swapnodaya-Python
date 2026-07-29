#LOGIN,REGISTRATION AND 
# UPDATE THE EMAIL REGISTRATION TO WARN UPPERCASE AND 
# WARN FIRST NAME SHOULD BE MORETHAN ONE CHARACTER,
# CODE TO VALIDATE . AND @ IN EMAIL
# PASSWORD SHOULD BE 8 CHARACTERS, UPPERCASE,LOWERCASE,DIGIT,SYMBOL
#ADD ANOTHER FUNCTIONALITY FORGET PASSWORD, AND SHOW YOUR PASSWORD HASBEEN UPDATED TO THIS...
list = {}
def user_registration():
    First_name = input("enter the first name:")
    Last_name = input("enter the last name:")
    Email = input("enter the email:")
    Password = input("enter the password:")
    if Email in list:
        print("User already exists. Please login.")
    else:
        print("Registration successful.")
def user_login():
    Email = input("enter the email:")
    Password = input("enter the password:")
    if Email in list or Password == True:
        print(f"{First_name} logged in successfully.")
    elif Email not in list or Password == False:
        print("Either email or password doesn't match. Please try again.")
    else:
        print("User not found! Please register")
def main():
    while True:
        choice = input("choose an option(1-3):").strip()
        print("1 Register")
        print("2 Login")
        print("3 Invalid choice")

        if choice == "1":
            user_registration()
        elif choice == "2":
            user_login()
        elif choice == "3":
            print("good bye")
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()
            
        
    
