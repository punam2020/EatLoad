def password(pwd):
    if len(pwd) > 6 or len(pwd) < 10:
        return True
    else:
        return False


def phone_no(mobile):
    if len(mobile) > 10:
        return False
    elif len(mobile) == 10:
        return True
    elif mobile.isalpha():
        return False
    else:
        return False


def otp(otp_no):
    if len(otp_no) > 6:
        return False
    elif otp_no == "":
        return False
    else:
        return True


def register():
    mobile = True
    while mobile:
        phone_num = input("enter phone no")
        val = phone_no(phone_num)
        if val:
            print("your phone no is {}".format(phone_num))
            mobile = False

    otp_var = True
    while otp_var:
        otp_num = input("enter otp number")
        result = otp(otp_num)
        print(result)
        if result:
            print("your otp no.is {}".format(otp_num))
            otp_var = False

    password_var = True
    while password_var:
        pwd = input("enter your password: ")
        confirm_pwd = input("enter confirm password : ")
        password(pwd)
        if pwd == confirm_pwd:
            print("successfully registered")
            password_var = False


register()
