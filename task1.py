# Initial user data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# Create
def add_user(user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email})
    print(f"User with ID {user_id} added.")

# Read
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Update
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print(f"User with ID {user_id} updated.")
            return
    print(f"User with ID {user_id} not found.")

# Delete
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    print(f"User with ID {user_id} deleted.")

# Main (for testing)
if __name__ == "__main__":
    # Add user
    add_user(3, "Charlie", "charlie@example.com")

    # Get user
    user = get_user(2)
    print("Retrieved user:", user)

    # Update user
    update_user(1, name="Alice Cooper")

    # Delete user
    delete_user(2)

    # Final list
    print("Final user list:", users)
