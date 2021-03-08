def pass_check(password):
    if len(password) < 8:
        return False
    number_count = 0
    for char in password:
        if not char.isalnum():
            return False
        if char.isdigit():
            number_count += 1

    if number_count < 2:
        return False
    return True


def main():
    print("Create Password: ", end='')
    password = input()
    while not pass_check(password):
        print("Invalid Password, try again...")
        print("Enter Password: ", end='')
        password = input()
    print('valid password')


if __name__ == '__main__':
    main()
