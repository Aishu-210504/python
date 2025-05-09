import re

def is_valid_email(email):
    # Regex pattern for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Main code
if __name__ == "__main__":
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")
