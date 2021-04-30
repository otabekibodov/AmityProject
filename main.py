""" 
Iterating through functions
"""

#global variable
UI = "\n1.Login\n2.Search for tools\n3.Create new account\n4.Exit\n"


# login to account function
def login():
    isfound=False
    login_file = open("login.txt", "r")
    username = input("Enter your username: ")
    password = input("Enter password: ")
    for line in login_file:
        if username in line:
            if username == line.split()[0] and password == line.split()[1]:
                isfound = True
                print("Welcome, " + username)
    if not isfound:
        print("Wrong username or password!")
    login_file.close()


# tools entry
def tools():
    tools_file = open("tools.txt", "r")
    tool = input("Search: ")
    isfound = False
    for line in tools_file:
        if tool in line:
            isfound = True
            print(line, end='')
    if not isfound:
        print("Tool not found")
    tools_file.close()
        


# create account fucntion
def create():
    login_file = open("login.txt", "w")
    name = input("Your username: ")
    while True:
        password = input("Enter new password: ")
        confirmation = input("Re-enter your password: ")
        if password == confirmation:
            break
        else:
            print("Password not match! Please re-enter passwords.")
    login_file.write(name + ' ' +password + '\n')
    login_file.close()
    


def cli():
    uinput = 0
    while True:
        print(UI)
        uinput = int(input("Enter your choice: "))
        if uinput == 1:
            login()
        elif uinput == 2:
            tools()
        elif uinput == 3:
            create()
        else:
            print("(exit)")
            break

if __name__ == '__main__':
    cli()
