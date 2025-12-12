import os
print("Welcome to my")
print("==================================")
print("SIMPLE PROGRAM FOR TEACHING PYTHON")
print("==================================")
print("")

while True:
    x = input("Type (next) Here to Start ---> ").lower()
    if x == "next":
        os.system("cls")
        print("Our Topics:")
        print("[1] - Python introduction")
        print("[2] - What is Variable and Print Output")
        print("[3] - Data Types")
        print("[4] - Input Function")
        print("[5] - Types of Operators")
        print("[6] - Conditional statements")
        print("[7] - Loop statement")
        print("[8] - List and Dictionary")
        print("[10] - function")
        print("[10] - import")
        print("[x] - Exit program")

        choice = input("""To start the program type the CODE the code is the one inside this "[]": """)

        if choice == "1":
            os.system("cls")
            print("Python INtroduction")
            print("Python is both simple and powerful, it allows you to write very simple scripts and " \
            "thanks to its many libraries, you can work on more ambitious projects. " \
            "\n\n#Sabi nga nila parang nag babasa at nag susulat ka lang in English dito kay python. ")
            exit = input("\n[X]Exit Python Introduction").lower()
            if exit == "x":
                os.system("cls")
                print("Exited Python Introduction")
                continue
        elif choice == "2":
            os.system("cls")
            print("What is Variable and Print Output")
            print("\nVARIABLE "
            "\nit is a container that stores information.You give it a name, \nand you can put a value inside it like a number, word, or sentence." \
            "\n#- Ito ay isang lagayan o ating bag na ginagamit \npara mag lagay ng bagay sa loob na tinatawag nating VALUE")
            print("\nEXAMPLE:" \
            "\nmy_name = gilcris" \
            "\n#etong nakalagay na 'my_name' yan ang ating variable at ang kanyang value ay 'gilcris'")
            print("======================================================================================")
            print("\nNOTE:" \
            "\nkung makikita mo may equal sign na nasa gitna ng variable at value" \
            "\ntinatawag natin itong assignment operator which is ito ang nagiging" \
            "\nway para maging connected na ang variable at value")
            print("======================================================================================")

            exit = input("\n[next] - proceed to the next topic PRINT"
            "\nOR"
            "\n[X]Exit What is Variable and Print Output: ").lower()
            if exit == "x":
                os.system("cls")
                print("Exited What is Variable and Print Output")
                continue
            elif exit == "next":
                os.system("cls")
                print("PRINT")
                print("- It is a built in function that is used  to display an output to the console")
                print("#- Eto ang ginagamit natin para maipakita sa ating screen ang mga output" \
                "\nkagaya netong mga binabasa mo ngayon lahat ng binabasa mo ngayon ay ginamitan ko ng print function")
                print("\nPaano nga ba gamitin ang print function?" \
                "\n#eto o " \
                "\nprint() \t#<---- yeps yan na yung print function")
                print("\n#So para nga magamit yan mag lalagay lang tayo Double Qoutes sa loob neto()" \
                "\nParang ganto: \nprint(\"\") " \
                "\n\n#ngayon lagyan mo naman ng laman ang double qoutes ng kahit ano but try this first" \
                "\neto ba:" \
                "\nprint(\"Hello World!\")")
                print("result on your console:" \
                "\nHello World!")
                print("We can also print variables. \nEXAMPLE:" \
                "\nb = \"boy\"" \
                "\nprint(b)")
                print("result on your console:" \
                "\nboy")


                print("\nCONGRATS PO PRORAMMER KA NA!!!")

                exit=input("[X] Exit What is Variable and Print Output: ").lower()
                if exit == "x":
                    os.system("cls")
                    print("Exited What is Variable and Print Output")
                else:
                    print("INVALID INPUT")
        elif choice == "3":
            os.system("cls")
            print("DATA TYPES")
            print("- In Data Types We have 4 that we will frequently use in programming it is the\nstring, integer, float, boolean.")
            print("\n1. String(str) - this is the string it is used to represent and store sequence of" \
                  "\ncharacters. These characters can include letters, symbols, and  spaces.")
            print("\t       - ito ay ginagamit para mag- represinta o mag-lagay ng iba't iabng uri" \
                  "\nkarakter. Ang mga karakter ay binubuo ng mga letra, simbolo, at agwat.")
            print("EXAMPLE:" \
                  """\nname =  "Gilcris" \nmessage = \"hello world!\"""")
            print("\n2. Integer(int) - this is the integer it is used to represent whole numbers," \
                  "\nfactorial and decimals are not included.")
            print("\t        - ito ay ginagamit para irepresenta ang mga buong numero, ang factorial at" \
                  "\ndesimal ay hindi nabibilang.")
            print("EXAMPLE:" \
                  "\nage = 18 \nyear = 2025")
            print("\n3. Float point(float) - this is float point it si used to represent real numbers, " \
                  "\nlike fractional and decimal numbers.")
            print("\t\t      - ito ay ginagamit para irepresenta at pag-gamitan ng mga real numbers," \
                  "\nkagaya ng fractional at desimal numbers.")
            print("EXAMPLE:" \
                  "\nprice = 19.99 \ngpa = 3.1")
            print("\n4. Boolean(bool) - this is boolean it is used to represent boolean values," \
                  "\n which is fundamental for expresing truth values in logic programming" \
                    "\nbool values: truth and false")
            print("\t         - ito ay ginagamit para irepresenta ang boolean values," \
                  "\nkung dssn mahalaga para ipakita ang truth values sa  logical programming" \
                  "\nbool values: truth and false")
            print("EXAMPLE" \
                  "\ngreen = true \nred = false")
            print("\nCONGRATS YOU ARE GROWING AS A PROGRAMMER:)")
            exit=input("[X] Exit DATA TYPES: ").lower()
            if exit == "x":
                os.system("cls")
                print("Exited DATA TYPES")
            else:
                print("INVALID INPUT")

        elif choice == "4":
            os.system("cls")
            print("INPUT FUNCTION")
            print("""input()""")
            print("- input function is used to obtain input from the user via the keyboard. This function pauses " \
            "the program's execution, \nwaits for the user to type something and press Enter, and then returns the entered value as a string.")
            print("#Ginagamit natin ang input para kumuha ng data from the user pwede rin nating ilagay sa isang" \
            "\n variable ang input function para i save ang data na nilagay ng user")
            print("\nHere's an example on how to use it:")
            
            print("""x = input("user_input = input(\"\")")
            \nprint(x)""")
            print("If we run this code it will show this:")
            print("==========")
            X = input("")
            print(X)
            print("==========#design lang tong mga equal sign ahHEHE")
            print("\nNOTE" \
            "\n- We can also put words in the input function like this" \
            "\nx = input(\"Can I ask you something? \")")
            print("====================================")
            x = input("Can I ask you something?")
            print(x)
            print("====================================")
            print("- We also need to put a space in the end of the sentence or before the last Double Quotes" \
            "\ninside the input functiion. It is because jan nag lalagay ang user ng input")
            print("CONGRATS AGAIN!!!" \
            "\nYou Have Learned Something New Nanaman:)")
            
            exit=input("\n[X] Exit INPUT FUNCTION: ").lower()
            if exit == "x":
                os.system("cls")
                print("Exited DATA TYPES")
            else:
                print("INVALID INPUT")

        elif choice == "5":
            os.system("cls")
            while True:
                print("TYPES OF OPERATORS")
                print("\n[1] - ARITHMETIC OPERATORS\n\n[2] - ASSIGNMENT OPERATORS\n\n[3] - RELATIONAL OPERATORS\n\n[4] - LOGICAL OPERATORS")
                x = str(input("TYPE HERE THE CODE YOU WANT TO START ---> "))
                if x == "1":
                    os.system("cls")
                    print("ARITHMETIC OPERATORS")
                    print("- This OPERATOR is used in computations")
                    sign = ['+','-','/','*','**','//','%']
                    sign1 = ['Addition','Subtraction','Division','Multiplication','Exponentstion','Floor division(integer division)','Modulus Division(remainder)']
                    for i in sign:
                        print(f"[{i}] - {sign1}")
                    
                elif x == '2':
                    os.system("cls")
                    print("ASSIGNMENT OPERATORS")
                    print("- It is used to assign values to variables")
                    print("\nCOMMON OPERATOR LIST" \
                    "\n= - Assignment - x = 5" \
                    "\n+= - Addition assignment - x += 3" \
                    "\n-= - Subtraction assignment - x -= 3" \
                    "\n*= - Multiplication assignment = x *= 3" \
                    "\n/= - Divisioin assignment - x /= 3" \
                    "\n%= - Modulus assignment - x %= 3" \
                    "\n**= - Exponentation assignment - x **= 3" \
                    "//= - Floor division assignment - x //= 3 ")
                elif x == '3':
                    print("RELATIONAL OPERATORS")
                    print("Use to compare two values and return a Boolean result (True or False)")
                    print(" 6 main relational operators" \
                    "== - Equal to - True if values are equal otherwise  False." \
                    "\n\n!= - Not equal to - True if values are not equal, otherwise false" \
                    "\n\n> - Greater than - True if the left value is greater than the right" \
                    "\n\n< - Greater than - True if the right value is greater than the left" \
                    "\n\n>= - Greater than or equal to - True if the left value is greater than or equal to the right" \
                    "\n\n<= - Less than or equal to - True if the right value is greater than or equal to the left")
                elif x == '4':
                    print("LOGICAL OPERATORS")
                    print("AND OR NOT")
                    print("and = Returns True if both statements are True otherwise False." \
                    "\n\nor - Returns true if at least one of the statement is True otherwise. False" \
                    "\n\nnot - Reverse the logical state of its value: Returns false if the condition is True, Returns False if the condition is True. ")
                else:
                    os.system("cls")
                    ("Maybe you typed something wrong?")
                    continue
                


        elif choice == "6":
            print("CONDITIONAL STATEMENT")

        elif choice == "7":
            print("LOOP STATEMENT")
        elif choice == "8":
            print("LIST AND DICTIONARY")
        elif choice == "9":
            print("IMPORT")
        elif choice == "x":
            os.system("cls")
            print("EXIT PROGRAM")
            break
        else:
            os.system("cls")
            print("INPUT INCORRECT")
            continue
    else:
        print("Maybe you typed the word (NEXT) Incorrectly?")

        

        