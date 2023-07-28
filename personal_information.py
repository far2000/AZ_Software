import re


def get_name():
    name = input("please enter your name: ")
    return name

def get_last_name():
    last_name = input ("please enter your last name: ")
    return last_name

def get_email_address():
    return email_validate( input("please enter your email address: "))
     

def email_validate(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return email
    else:
      return "invalid email address"


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

def appearance_information():
    try:
        hight = isinstance(input("please enter your hight in integer: "), int)
    except:
        return None
    
    hair_colour = input("please enter your hair colour (black\ brown\ yellow\ others): ")
    if hair_colour == "black":
        hair_colour = "black"
    elif hair_colour == "brown":
        hair_colour = "brown"
    elif hair_colour == "yellow":
        hair_colour = "yellow"
    elif hair_colour == "others":
        hair_colour = "others"
    else:
        hair_colour = "prefer not to say"
    
    eye_colour = input ("pleae enter your eye colour (black\ blue\ green\ brown\ others): ")
    if eye_colour == "black":
        eye_colour = "black"
    elif eye_colour == "brown":
        eye_colour = "brown"
    elif eye_colour == "green":
        eye_colour = "green"
    elif eye_colour == "blue":
        eye_colour = "blue"
    elif eye_colour == "others":
        eye_colour = "others"
    else:
        eye_colour = "prefer not to say"
    
    skin_colour = input("please enter your skin colour (black\white\yellow\others): ")
    if skin_colour != "black" or skin_colour != "white" or skin_colour != "yellow" or skin_colour != "others":
        skin_colour = "prefer not to say"
    
    return (f"hight: {hight}", f"skin colour: {skin_colour}", f"hair colour: {hair_colour}", f"hair colour: {eye_colour}")

def print_information(name, last_name, phone_number, email_address, 
                      address, gender, job, degree, age, appearance):
    print(f"name: {name}\nlast name: {last_name}\nage: {age}\ngender: {gender}\nphone number: {phone_number}\n email address: {email_address}\naddress: {address}\njob: {job}\ndegree: {degree}" )
    for i in appearance:
        print(i)




def main():
    name = get_name()
    last_name = get_last_name()
    age = get_age()
    gender = gender_check()
    phone_number = get_phone_number()
    email_address = get_email_address()
    address = get_address()
    job = get_job()
    degree = degree_check()
    appearance = appearance_information()
    print_information(name, last_name, phone_number, email_address, 
                      address, gender, job, degree, age, appearance)

if __name__ == "__main__":
    main()

