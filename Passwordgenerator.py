import random
import string

def generate_password(length, complexity):
   

    characters = string.ascii_letters + string.digits

    if complexity == "medium":
        characters += string.punctuation
    elif complexity == "high":
        characters += string.printable

    return "".join(random.choice(characters) for _ in range(length))

def main():
  

  
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

   
    while True:
        complexity = input("Choose password complexity (low, medium, high): ").lower()
        if complexity not in ["low", "medium", "high"]:
            print("Invalid complexity option. Please enter low, medium, or high.")
        else:
            break

    # Generate and display password
    password = generate_password(length, complexity)
    print("Your generated password:", password)

    # Ask for confirmation and handle user response
    while True:
        choice = input("Do you want to generate another password ? (y/n): ").lower()
        if choice == "y":
             complexity = input("Choose password complexity (low, medium, high): ").lower()
             length = int(input("Enter desired password length (minimum 8): "))
             if length < 8:
                print("Password length must be at least 8 characters.")
             
             password = generate_password(length, complexity)
             print(password)
        elif choice == "n":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter y or n.")

if __name__ == "__main__":
    main()

