import validator_collection

def main():
    email = input("Email: ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

def is_valid_email(email):
    val = validator_collection.checkers.is_email(email)
    return val

if __name__ == "__main__":
    main()
