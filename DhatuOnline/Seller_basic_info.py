def Basic_info():
    name_company = input("enter company name")
    print(name_company)

    ''' enter constitution of company'''
    constituion_var = True
    while constituion_var:
        constitution_of_comapny = {"1": "Public Limited", "2": "Private Limited", "3": "Partnership", "4": "LLp",
                                   "5": "Proprietorship"}
        constitution_of_input_company = input("Enter constitution of company : ")

        if constitution_of_input_company in constitution_of_comapny.keys():
            print(constitution_of_comapny.get(constitution_of_input_company))
            constituion_var = False
        else:
            print("give valid input")

    company_catogory = True
    while company_catogory:
        company_catogory = {"1": "Micro", "2": "Small", "3": "Medium", "4": "Large"}
        company_input_catogory = input("Enter company catogory: ")

        if company_input_catogory in company_catogory.keys():
            print(company_catogory.get(company_input_catogory))
            company_catogory = False
        else:
            print("Invalid input")
    Manufacturer = True
    while Manufacturer:
        Manufacturer = {"1": "Manufacturer", "2": "Trader1", "3": "Trader2", "4": "Trader3"}
        Manufacturer_input = input("Enter Manufacturer name: ")
        if Manufacturer_input in Manufacturer.keys():
            print(Manufacturer.get(Manufacturer_input))
            Manufacturer = False

        else:
            print("invalid input")
    address = input("Enter Your Address: ")
    print(address)
    country = True
    while country:
        country = {"1": "India", "2": "Australia", "3": "Japan", "4": "Canada"}
        country_input = input("select your country: ")
        if country_input in country.keys():
            print(country.get(country_input))
            country = False
        else:
            print("invalid input")

    city = True
    while city:

        city = {"1": "Mumbai", "2": "Chennai", "3": "Bangalore", "4": "Delhi"}
        city_input = input("Enter your city")
        if city_input in city.keys():
            print(city.get(city_input))
            city = False


        else:
            print("invalid input")
    state = True
    while state:
        State = {"1": "Karnatak", "2": "Odisha", "3": "Delhi", "4": "Tamilnadu"}
        State_input = input("Enter Your state")
        if State_input in State.keys():
            print(State.get(State_input))
            state = False

        else:
            print("Invalid input")

    pincode = (input("enter pincode"))
    value = validate_pin(pincode)
    print(value)
    Registered_mobile_number = (input("enter registered mobile number"))
    res = mobile(Registered_mobile_number)
    print(res)
    email_id = input("enter your email: ")
    val = email(email_id)
    print(val)

    corporate_phone_number = (input("enter corporate phone number"))
    res1 = mobile(corporate_phone_number)
    print(res1)
    Branch_phno = (input("enter branch phone number"))
    res2 = mobile(Branch_phno)
    print(res2)
    contact_person = (input("enter your name"))
    result1 = person(contact_person)
    print(result1)
    Designation = input("enter designation")
    result2 = person(Designation)
    print(result2)
    email_id = input("enter your email: ")
    val = email(email_id)
    print(val)


def mobile(phone):
    for x in phone:
        if x.isalpha():
            return False
        elif len(phone) == 10:
            return True
        else:
            return False

    return phone


def person(people):
    for x in people:

        if x.isalpha():
            return True
        else:
            return False
    return people


def email(email):
    if '@' in email and 'gmail' in email and '.' in email:
        return ("your email is{}".format(email))
    else:
        print("invalid email")


def validate_pin(pin):
    for x in pin:
        if x.isalpha():
            return False
        elif len(pin) == 6:
            return True
        else:
            return False
    return pin


Basic_info()
