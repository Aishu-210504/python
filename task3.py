import hashlib

# Dictionary to store username: hashed_password
users = {}

# Function to hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register function
def register(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print("Created new user.")

# Login function
def login(username, password):
    hashed = hash_password(password)
    if users.get(username) == hashed:
        print("Login Successful.")
    else:
        print("Invalid username or password.")

# Main code for testing
if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            register(uname, pwd)
        elif choice == "2":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            login(uname, pwd)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
