def phone_no(mobile):
    if len(mobile) > 10:
        return False
    elif len(mobile) == 10:
        return True
    elif mobile.isalpha():
        return False
    else:
        return False


option = {"1": "registered mobileno", "2": "registered Emailid"}
choice = input("two option is there select one of them 1/2 : ")
if option[choice] == "registered mobileno":
    register_mobile = True
    while register_mobile:
        phone_num = input("enter phone no")
        val = phone_no(phone_num)
        if val:
            print("your phone number is".format(phone_num))
            register_mobile = False
            old_pwd = "password"
            new_pwd = input("enter your password")
            if old_pwd != new_pwd:
                print("your password successfully changed")
            else:
                print("renter your password ")

if option[choice] == "registered Emailid":
    email_var = True
    while email_var:
        email_id = input("enter email")
        print(email_id)
        email_var = False
    old_pwd = "password"
    new_pwd = input("enter your password")
    if old_pwd != new_pwd:
        print("your password successfully changed")
    else:
        print("renter your password ")
