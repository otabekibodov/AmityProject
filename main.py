""" 
Iterating through functions
"""
entrance = 0
UI = "1. Login\n2.search for tools\n3.create new account\n4.exit"
while entrance <= 4:
    print(UI)
    entrance = input("Enter your choice: ")
    if entrance == "1":
        login()
    elif entrance == "2":
        tools()
    elif entrance == "3":
        create()
    else:
        exit
def login():
    login_file = open("login.txt", "r")
    username = input("Enter your username: ")
    password = input("Enter password: ")
def tools():
    tools_file = open("tools.txt", "rw")
    tool = input("Search: ")
def create():
    login_file = open("login.txt", "w")
    name = input("your name: ")
    phone = input("your number: ")
    date_of_birth = input("Enter your date of birth: ")
    new_login = ("Enter username: ")
    password = ("Enter new password: ")
    confirmation = ("Re-enter your password: ")
