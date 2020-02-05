def Registration():
    gstin = input("Enter gstin: ")
    quality_mngt_sys = input("Enter quality management sytem: ")
    turnover_last_3years = {"1": "2016-2017", "2": "2017-2018", "3": "2018-2019"}
    turnover_input = input("enter  turnover_last_3years ")
    if turnover_input in turnover_last_3years.keys():
        print(turnover_last_3years.get(turnover_input))
    else:
        print("Invalid input")
        exit()
    add_bank = []
    while True:
        bank = input("select your bank")
        if bank == '':
            break
        add_bank.append(bank)
    print(add_bank)
    add_term_payment = []
    while True:
        term_payment = input("enter terms of payment")
        if term_payment == '':
            break
        add_term_payment.append(term_payment)
        print(add_term_payment)
    exit()


Registration()
