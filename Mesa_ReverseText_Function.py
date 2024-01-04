def get_user_input():
    while True:
        user_input = input("Enter a string: ")
        if not user_input.isdigit():
            return user_input
        else:
            print("Error Reported! Enter text only.")

def reverse_text(input_text):
    reversed_text = input_text[::-1]
    return reversed_text

def main():
    while True:
        user_input = get_user_input()
        reversed_text = reverse_text(user_input)
        print("Output:", reversed_text)

if __name__ == "__main__":
    main()

