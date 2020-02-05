def product_info():
    add_product = []
    while True:
        product_information = input("Enter product name: ")

        if product_information == '':
            break
        add_product.append(product_information)
    print(add_product)


product_info()
print("THANK YOU FOR REGISTRATION ON DHATUONLINE")
