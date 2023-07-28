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

def get_job():
    job = input("please enter your job: ")
    return job

def degree_check():
    degree = input("please enter your degree (Associate\ Bachelor's\ Graduate\ Professional\ no degree): ")

    if degree == "Associate":
        return "Associate"
    elif degree == " Bachelor's":
        return " Bachelor's"
    elif degree == "Graduate":
        return "Graduate"
    elif degree == "Professional":
        return "Professional"
    elif degree == "no degree":
        return "no degree"
    else:
        return None

def get_age():
    try:
        age = isinstance(input("please enter your age in integer: "), int)
        return age
    except:
        return None

def get_phone_number():
    phone_number = input("please enter your phone number: ")
    return phone_number


def main():
    name = get_name()
    last_name = get_last_name()
    phone_number = get_phone_number()
    email_address = get_email_address()
    address = get_address()
    gender = gender_check()
    job = get_job()
    degree = degree_check()
    age = get_age()
    appearance = ""

if __name__ == "__main__":
    main()

