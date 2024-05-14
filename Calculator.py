# To input any two numbers by the user
number_1 = int(input("Enter first number -: "))
number_2 = int(input("Enter second number -: "))

while True:
    print("\n\n1. + \n2. - \n3. * \n4. / \n5. ALL \n6. EXIT")

    operation = int(input("Enter arithmetic operation (1,2,3,4) -: "))
    print("\n")
# conditions used for operations
    if (operation == 1):
        print("SUM -: ", number_1+number_2)

    elif (operation == 2):
        print("SUBTRACT -: ", number_1 - number_2)

    elif (operation == 3):
        print("PRODUCT -: ", number_1 * number_2)

    elif (operation == 4):
        print("DIVIDE -: ", number_1/number_2)

    elif(operation == 5):
        print("SUM -: ", number_1+number_2)
        print("SUBTRACT -: ", number_1 - number_2)
        print("PRODUCT -: ", number_1 * number_2)
        print("DIVIDE -: ", number_1/number_2)


    elif(operation == 6):
        print("Quiting")
        break

    else:
        print("Worong Operator")