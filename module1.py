import csv

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        self.users.append(User(username, password))

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

auth_system = AuthenticationSystem()

while True:
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Login")
        username = input("Username: ")
        password = input("Password: ")
        
        if auth_system.login(username, password):
            print("Login successful.")
            break
        else:
            print("Incorrect username or password. Please try again.")
            
    elif choice == "2":
        print("Register")
        username = input("Username: ")
        password = input("Password: ")
        auth_system.register_user(username, password)
        print("Registration successful. You can now log in.")
        
    elif choice == "3":
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")
