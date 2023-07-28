def get_name():
    name = input("please enter your name: ")
    return name



def get_last_name():
    last_name = input ("please enter your lasr name: ")
    return last_name

def get_email_address():
    email_address = input("please enter your email address: ")
    return email_address


def main():
    name = get_name()
    last_name = get_last_name()
    phone_number = input("please enter your phonr number: ")
    email_address = get_email_address()
    address = input("please enter your address: ")
    gender = input("please enter your gender (female\male\others): ")
    job = input("please enter your job; ")
    degree = input("please enter your degree (Associate\ Bachelor's\ Graduate\ Professional): ")
    age = input("please enter your age (integer): ")
    appearance = ""

if __name__ == "__main__":
    main()

