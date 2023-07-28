def get_name():
    name = input("please enter your name: ")
    return name



def get_last_name():
    last_name = input ("please enter your lasr name: ")
    return last_name

def get_email_address():
    email_address = input("please enter your email address: ")
    return email_address

def get_address():
    address = input ("please enter your address: ")
    return address

def gender_check():
    gender = input("please enter F for female, M for male and O for others: ")
    if gender == 'F'or gender == 'f':
        return "Female"
    
    elif gender == 'M'or gender == 'm':
        return "Male"
    
    elif gender == 'O'or gender == 'o':
        return "Others"
    else:
        return None

def main():
    name = get_name()
    last_name = get_last_name()
    phone_number = input("please enter your phonr number: ")
    email_address = get_email_address()
    address = get_address()
    gender = gender_check()
    job = input("please enter your job; ")
    degree = input("please enter your degree (Associate\ Bachelor's\ Graduate\ Professional): ")
    age = input("please enter your age (integer): ")
    appearance = ""

if __name__ == "__main__":
    main()

